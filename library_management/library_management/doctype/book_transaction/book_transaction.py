import frappe
from frappe.utils import today
from frappe import _
from frappe.model.document import Document
from frappe.utils import nowdate, getdate


class BookTransaction(Document):
    def validate(self):
        # for rt in self.book_transaction_detail:
        #     rt_data = frappe.db.get_value('Book Ledger',rt.access_no,['member'])
        #     self.member = rt_data
        pass

    @frappe.whitelist()
    def on_submit(self):
        self.create_book_ledger()
        self.on_submit_asset_update()
        self.membership_validate()
        # barcode = frappe.get_doc('Book Transaction', self.barcode)
        # self.find_asset_by_barcode(barcode)

    def on_submit_asset_update(self):
        try:
            # Determine the table to fetch data from based on transaction type
            table_name = "Book Transaction Detail" if self.transaction_type == "Issue" else "Return Book Details"

            # Fetch book transaction details
            book_detail_table = frappe.get_all(
                table_name,
                filters={"parent": self.name},
                fields=["access_no"],
            )

            for asset in book_detail_table:
                access_no = asset.get("access_no")
                if access_no:
                    # Fetch asset document
                    asset_doc = frappe.get_doc("Asset", access_no)
                    if asset_doc:
                        # Update status based on transaction type
                        if self.transaction_type == "Return":
                            asset_doc.status = "Available"
                            asset_doc.save()
                            frappe.msgprint(f"Asset {access_no} updated successfully")
                        else:
                            asset_doc.status = self.transaction_type
                            asset_doc.save()
                            frappe.msgprint(f"Asset {access_no} updated successfully")

                        # asset_doc.status = self.transaction_type
                        # asset_doc.save()
                        # frappe.msgprint(f"Asset {access_no} updated successfully")
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), "Asset Update Error")
            frappe.throw(f"An error occurred while updating assets: {str(e)}")


    def membership_validate(self):
        try:
            # Fetch membership details
            membership_service = frappe.get_all(
                'Membership Details',
                filters={'parent': self.member},
                fields=['membership_status', 'due_date', 'library_service']
            )
            
            # Check if there is any active membership
            is_active = False
            current_date = getdate(nowdate())

            for ms in membership_service:
                library_service_name = ms.get('library_service')
                #frappe.msgprint(f"Service Name: {library_service_name}")
                
                if library_service_name:
                    # Run SQL query to get the checkbox value
                    query = """
                    SELECT take_a_book_from_library
                    FROM `tabLibrary Service`
                    WHERE name = %s
                    """
                    result = frappe.db.sql(query, (library_service_name,), as_dict=True)
                    
                    # Check if any result is returned
                    if result:
                        book_issue_check = result[0].get('take_a_book_from_library')
                        # frappe.msgprint(f"Book Issue Check: {book_issue_check}")
                        
                        # Check if membership is active, not expired, and allowed to issue books
                        if ms.get('membership_status') == 'Active' and (not ms.get('due_date') or ms.get('due_date') >= current_date) and book_issue_check == 1:
                            is_active = True
                            # frappe.msgprint("Membership is active and member is allowed to issue books.")
                            break
                    else:
                        frappe.msgprint(f"No record found in Library Service with name: {library_service_name}")
                else:
                    frappe.msgprint("No library service associated with this membership detail.")
                
            # If no active membership found, or not allowed to issue books, raise an exception
            if not is_active:
                frappe.throw(_('The member does not have an active membership or is not allowed to issue books.'))

        except Exception as e:
            # Handle exceptions
            frappe.log_error(frappe.get_traceback(), _('Membership Validation Error'))
            frappe.throw(_('An error occurred while validating membership: {0}').format(str(e)))

    def create_book_ledger(self):
        if self.transaction_type == "Issue":
            try:
                # Fetch only necessary fields from the child table
                book_transaction_details = frappe.get_all(
                    "Book Transaction Detail", filters={"parent": self.name}, fields=["*"]
                )
                for detail in book_transaction_details:
                    book_ledger_entry = frappe.new_doc("Book Ledger")
                    book_ledger_entry.member = self.member
                    book_ledger_entry.transaction_no = self.name
                    book_ledger_entry.transaction_type = self.transaction_type
                    book_ledger_entry.voucher_type = self.doctype
                    book_ledger_entry.membership_status = self.membership_status
                    book_ledger_entry.access_no = detail.get("access_no")
                    book_ledger_entry.transaction_date = detail.get("transaction_date")
                    book_ledger_entry.due_date = detail.get("due_date")
                    book_ledger_entry.insert()
                    book_ledger_entry.submit()
                    frappe.msgprint("Book Ledger Entries created successfully.")

            except Exception as e:
                # Log the error for better debugging
                frappe.log_error(
                    "An error occurred while creating book ledger entries: {0}".format(
                        str(e)
                    )
                )
        elif self.transaction_type == "Return":
            try:
                # Fetch only necessary fields from the child table
                
                book_ledger_entry_all = frappe.get_all(
                    "Return Book Details", filters={"parent": self.name}, fields=["*"]
                )
                for bl in book_ledger_entry_all:
                    tn_no = bl.get("transaction_no")
                    bl_doc = frappe.get_doc("Book Ledger",tn_no)
                    bl_doc.return_date = bl.get("return_date")
                    bl_doc.overdue_day = (bl.get("return_date") - bl.get("due_date")).days
                    bl_doc.save()
                    frappe.msgprint("Book Ledger for return Update successfully")

            except Exception as e:
                # Log the error for better debugging
                frappe.log_error(
                    "An error occurred while creating book ledger entries: {0}".format(
                        str(e)
                    )
                )
        elif self.transaction_type == "Return":
            try:
                # Fetch only necessary fields from the child table
                book_transaction_details = frappe.get_all(
                    "Book Transaction Detail", filters={"parent": self.name}, fields=["*"]
                )
                for detail in book_transaction_details:
                    book_ledger_entry = frappe.new_doc("Book Ledger")
                    book_ledger_entry.member = self.member
                    book_ledger_entry.transaction_no = self.name
                    book_ledger_entry.transaction_type = self.transaction_type
                    book_ledger_entry.voucher_type = self.doctype
                    book_ledger_entry.membership_status = self.membership_status
                    book_ledger_entry.access_no = detail.get("access_no")
                    book_ledger_entry.transaction_date = detail.get("transaction_date")
                    book_ledger_entry.due_date = detail.get("due_date")
                    book_ledger_entry.insert()
                    book_ledger_entry.submit()
                    frappe.msgprint("Book Ledger Entries created successfully.")

            except Exception as e:
                # Log the error for better debugging
                frappe.log_error(
                    "An error occurred while creating book ledger entries: {0}".format(
                        str(e)
                    )
                )
                
    @frappe.whitelist()
    def on_cancle(self):
        self.cancel_book_ledger_entries()
        self.cancel_book_transaction()

    def on_cancel(self):
        try:
            # Fetch Book Ledger entries associated with the canceled Book Transaction
            book_ledger_entries = frappe.get_all(
                "Book Ledger", filters={"transaction_no": self.name}, fields=['name','access_no']
            )

            # Cancel each fetched Book Ledger entry
            for entry in book_ledger_entries:
                frappe.get_doc("Book Ledger", entry["name"]).cancel()
                if entry.get("access_no"):

                    asset_doc = frappe.get_doc("Asset", entry["access_no"])
                    if asset_doc:
                        if self.transaction_type == "Issue":
                            # Update the Asset status; adjust based on your specific requirements
                            asset_doc.status = "Available"  # or any other status you require
                            asset_doc.save()
                            frappe.msgprint(f"Asset {entry['access_no']} status updated to {asset_doc.status}.")
                        else:
                            asset_doc.status = "Issue"  # or any other status you require
                            asset_doc.save()
                            frappe.msgprint(f"Asset {entry['access_no']} status updated to {asset_doc.status}.")

            frappe.msgprint("Book Ledger Entries canceled successfully.")

        except Exception as e:
            frappe.msgprint(
                _("An error occurred while canceling Book Ledger entries: {0}").format(
                    str(e)
                )
            )

    @frappe.whitelist()
    def get_asset_by_barcode(self):
        transaction_doc = frappe.parse_json(self)
        barcode = transaction_doc.get("scan_barcode")
        transaction_type = transaction_doc.transaction_type

        
        if not barcode:
            frappe.msgprint(_("Please scan a barcode to fetch the asset details."))
            return

        filters = {
            "name": barcode,
        }
        if transaction_type == "Issue":
            filters["status"] = "Available"
        elif transaction_type == "Return":
            filters["status"] = "Issue"
        
        asset = frappe.db.get_value(
            "Asset", filters, ["name as asset_id", "item_code", "asset_name", "status"], as_dict=True
        )
        if not asset:
            return

        isbn_no = frappe.db.get_value("Book", asset.get("item_code"), "isbn")

        asset.update({"isbn": isbn_no})

        if transaction_type == "Return":
            member_details = frappe.db.get_value("Book Ledger", 
                {"access_no": barcode, "transaction_type": "Issue", "docstatus": 1}, 
                ["member", "name", "transaction_date", "due_date"],
                as_dict=True
            )
            asset.update({"member_details": member_details})
        
        return asset

@frappe.whitelist()
def fetch_member_issue_book_detail(first_access_no):
    member_details = frappe.get_value("Book Ledger", filters={"access_no":first_access_no,"transaction_type":"Issue","docstatus":1},fieldname=["member","name","transaction_date","due_date"], as_dict=True)
    frappe.msgprint(f"Working From Book Transaction")
    return(member_details)