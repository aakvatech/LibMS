import frappe
from frappe.utils import today, getdate
from frappe import _
from frappe.model.document import Document

class LibraryMembership(Document):

    def before_submit(self):
        duplicate_check_result = check_duplicate_membership(self.name, self.member)
        if duplicate_check_result.get('has_duplicate'):
            frappe.throw(_("Duplicate active membership service found: {0}").format(duplicate_check_result.get('duplicate_service')))
        
        self.membership_details_update()
        self.sales_invoice_created()

    def membership_details_update(self):
        """Update the membership details in the Member document."""
        try:
            # Fetch Library Membership Details
            library_membership_details = frappe.get_all('Library Membership Details',
                                                        filters={'parent': self.name},
                                                        fields=['*'])
            for details in library_membership_details:
                # Update the Member document
                member_doc = frappe.get_doc("Member", self.member)
                child_table_entry = member_doc.append("membership_details", {})
                child_table_entry.library_membership = self.name
                child_table_entry.library_service = details.get('library_service')
                child_table_entry.from_date = details.get('from_date')
                child_table_entry.due_date = details.get('due_date')
                child_table_entry.membership_status = details.get('service_status')
                member_doc.membership_status = details.get('service_status')
                member_doc.save()

        except Exception as e:
            frappe.msgprint(_("An error occurred while updating membership details: {0}").format(str(e)))

        
    def sales_invoice_created(self):
        customer = frappe.get_all('Customer', filters={'customer_name': self.member_name}, fields=["name"])
        
        try:
            if not customer:
                frappe.msgprint("Customer not found.")
                return

            if self.paid:  # Check if the membership is marked as paid
                invoice_doc = frappe.get_doc({
                    'doctype': 'Sales Invoice',
                    'customer': customer[0]['name'],
                    'items': []
                })

                # Fetch the library services from the Library Membership Details child table
                for detail in self.library_membership_details:
                    if not detail.library_service:
                        frappe.msgprint(f"Missing library service in detail: {detail}")
                        continue

                    if detail.amount is None:
                        frappe.msgprint(f"Missing amount in detail: {detail}")
                        continue

                    invoice_doc.append('items', {                   
                        'item_code': detail.library_service,
                        'item_name': detail.library_service,
                        'description': f"Service for {self.name}",
                        'qty': 1,
                        'rate': detail.amount
                    })

                if not invoice_doc.items:
                    frappe.msgprint("No items were added to the Sales Invoice.")
                    return

                invoice_doc.insert()
                # Uncomment the following line to automatically submit the invoice
                # invoice_doc.submit()
                self.invoice = invoice_doc.name
                frappe.msgprint(_("Sales Invoice created and submitted successfully: {0}").format(invoice_doc.name))

        except Exception as e:
            frappe.log_error(frappe.get_traceback(), _("Error during Sales Invoice creation"))
            frappe.msgprint(_("An error occurred while creating the sales invoice: {0}").format(str(e)))


@frappe.whitelist()
def check_duplicate_membership(document_name, member):
    """Check for duplicate memberships and ensure they are not active."""
    try:
        new_service = frappe.get_all('Library Membership Details',
                                     filters={'parent': document_name},
                                     fields=['*'])
        existing_service = frappe.get_all('Membership Details',
                                          filters={'parent': member},
                                          fields=['*'])

        for ns in new_service:
            for es in existing_service:
                if ns['library_service'] == es['library_service'] and es['membership_status'] == 'Active':
                    return {
                        'has_duplicate': True,
                        'duplicate_service': ns['library_service']
                    }

        return {'has_duplicate': False}
    except Exception as e:
        frappe.msgprint(f"An error occurred while checking for duplicate membership: {str(e)}")
        return {'has_duplicate': False}

@frappe.whitelist()
def auto_expire_memberships():
    """Automatically expire memberships and update the status in the child table."""
    try:
        memberships = frappe.get_all(
            "Library Membership", 
            filters={}, 
            fields=["name","member"]
        )
        current_date = getdate(today())  # Convert today's date to a date object

        for membership in memberships:
            membership_doc = frappe.get_doc("Library Membership", membership.name)
            member_id = membership_doc.member  # Directly access the member ID
            # frappe.msgprint(f"Member ID: {member_id}")
            # Iterate over the child table and update status
            for detail in membership_doc.library_membership_details:
                # Skip if membership_status is already 'Expired'
                if detail.service_status == "Expired":
                    frappe.msgprint(_("Skipping already expired service: {0}").format(detail.library_service))
                    continue

                if detail.due_date:
                    if getdate(detail.due_date) < current_date:
                        frappe.msgprint(_("Expiring service: {0}, due date: {1}").format(detail.library_service, detail.due_date))
                        detail.service_status = "Expired"
                        # member = frappe.get_all("Member",filters={'member':'member_id'},fields={'*'})
                        member = frappe.get_doc("Member", member_id)
                        # frappe.msgprint(f"Member Details: {member.as_dict()}")
                        for lm in member.membership_details:
                            if lm.library_membership == membership.name:
                                lm.membership_status = "Expired"
                        member.save()
                    else:
                        frappe.msgprint(_("Service: {0} is still active, due date: {1}").format(detail.library_service, detail.due_date))
                else:
                    frappe.msgprint(_("Service: {0} has no due date set").format(detail.library_service))

            membership_doc.save()

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Auto-expire memberships error"))
        frappe.msgprint(_("An error occurred during auto-expiration: {0}").format(str(e)))