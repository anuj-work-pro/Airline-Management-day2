import frappe
import random

def execute():
    tickets = frappe.get_all("Airplane Ticket", fields=["name"])

    for ticket in tickets:
		number=random.randint(1,99)
		choice=random.choice(['A','B','C','D','E'])
        seat = f"{number}{choice}"

        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)

    frappe.db.commit()
