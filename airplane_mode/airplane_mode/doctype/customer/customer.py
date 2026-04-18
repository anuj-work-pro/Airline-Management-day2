# Copyright (c) 2026, anuj and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class customer(Document):
    def after_insert(self):
          if self.custom_customer_name:
              self.custom_gst_number=self.custom_gst_number
	pass
