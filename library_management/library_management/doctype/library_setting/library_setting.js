// Copyright (c) 2024, ramjanali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Setting', {
	// refresh: function(frm) {

	// }
	uom(frm) {
        frappe.call({
            method: "library_management.custom_api.create_uoms",
            args: {
                member: "1"
            },
            callback: function(data) {
                
            }
        });
    }
});
