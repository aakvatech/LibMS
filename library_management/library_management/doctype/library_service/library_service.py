# Copyright (c) 2024, ramjanali and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibraryService(Document):
    def validate(self):
        self.create_from_library_service()
        
    def create_from_library_service(self):
        uom = frappe.get_value('Library Setting', 'library_service_uom','library_service_uom')
        if self.is_new():                
            item_doc = frappe.get_doc({
                'doctype': 'Item',
                'item_code': self.library_service,
                'item_name': self.library_service,
                'item_group': "Services",
                'is_stock_item': 0,
                'stock_uom': uom,
                'include_item_in_manufacturing': 0,
            })
            item_doc.insert()
            self.item_name = item_doc.name
            frappe.msgprint("Item created successfully")
