import frappe
import pyqrcode
import io
import base64


@frappe.whitelist()
def generate_qrcode(qrcode_data):
    c = pyqrcode.create(qrcode_data)
    s = io.BytesIO()
    c.png(s, scale=3,quiet_zone=1)
    encoded = "data:image/png;base64," + base64.b64encode(s.getvalue()).decode("ASCII")
    return encoded

@frappe.whitelist()
def count_books_issued(member):
    """
    Count the total books issued to the given member.
    """
    if not member:
        return {"count": 0}
    
    count = frappe.db.count("Book Ledger", filters={
        "member": member,
        "transaction_type": "Issue",
        "return_date": ["is", "null"],
        "docstatus": 1
    })

    # frappe.msgprint(f"Total books issued to the member: {count}")
    return {"count": count}

@frappe.whitelist()
def allowed_book(member):
    member_type = frappe.get_value("Member",filters={"name": member},fieldname="member_type")
    allowed = frappe.get_value("Member Type",filters={"name": member_type},fieldname="book_allowed")
    return(allowed)

@frappe.whitelist()
def fetch_member_issue_book_detail(first_access_no):
    member_details = frappe.get_value("Book Ledger", filters={"access_no":first_access_no,"transaction_type":"Issue","docstatus":1},fieldname=["member","name","transaction_date","due_date"], as_dict=True)
    return(member_details)

@frappe.whitelist()
def check_for_duplicates(document_name):
        """Check for duplicate memberships and ensure they are not active."""
        try:
            # Fetch new service details
            new_service = frappe.get_all('Library Membership Details',
                                         filters={'parent': document_name},
                                         fields=['*'])
            # Fetch existing service details from the Member
            existing_service = frappe.get_all('Membership Details',
                                              filters={'parent': document_name},
                                              fields=['*'])

            # Check for duplicates with active status
            for ns in new_service:
                for es in existing_service:
                    if ns['library_service'] == es['library_service'] and es['membership_status'] == 'Active':
                        frappe.throw(("Duplicate active membership service found: {0}").format(ns['library_service']))
                        return(document_name)
            # No duplicates found, proceed to add new service details
            
        except Exception as e:
            frappe.msgprint(("An error occurred while checking for duplicate membership: {0}").format(str(e)))

# @frappe.whitelist()
# def create_uom():
#     uom_name = "Quarterly"  # Replace with your desired UOM name
#     frappe.msgprint(f"UOM :{uom_name}")
#     if not frappe.db.exists("UOM", uom_name):
#         uom = frappe.get_doc({
#             "doctype": "UOM",
#             "uom_name": uom_name,
#             "enabled": 1
#         })
#         uom.insert(ignore_permissions=True)
#         frappe.msgprint(f"UOM :{uom_name}")
#         frappe.db.commit()

@frappe.whitelist()
def create_uoms():
    uom_names = ["Day", "Weekly", "Monthly", "Quarterly", "Half-yearly", "Yearly"]
    
    for uom_name in uom_names:
        # Check if UOM already exists
        if not frappe.db.exists("UOM", uom_name):
            uom_doc = frappe.get_doc({
                "doctype": "UOM",
                "uom_name": uom_name
            })
            uom_doc.insert()
            frappe.msgprint(f"UOM '{uom_name}' created successfully!")
        else:
            frappe.msgprint(f"UOM '{uom_name}' already exists.")


