// Copyright (c) 2023, ramjanali and contributors
// For license information, please see license.txt

//frappe.ui.form.on('Member', {
//	add_address: function(frm) {
            // Your client-side logic here
//            frappe.msgprint("Button Clicked!");
//        }
//});
frappe.ui.form.on('Member', {
    add_address: function (frm) {
        // Trigger the custom function when the button is clicked
            openNewDocType(frm);
    }
});
// Your custom function to open the new DocType
function openNewDocType(frm) {
    frappe.route_options = {
        // Set any default values for the new DocType fields here
        "address_title": frm.doc.name
    };
    frappe.new_doc("Address");
}
