# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe

from frappe import _

@frappe.whitelist()
def update_sales_invoice_from_address(address_name, sales_invoice_name):
    address = frappe.get_doc("Address", address_name)
    
    frappe.db.sql(""" update `tabSales Invoice` set
        organo_gestor=%s,
        oficina_contable=%s,
        unidad_tramitadora=%s,
        organo_proponente=%s
        where customer_address = %s
        and name = %s
    """, (address.organo_gestor, address.oficina_contable, 
        address.unidad_tramitadora, address.organo_proponente, 
        address_name, sales_invoice_name), debug=False)
    frappe.clear_cache(doctype="Sales Invoice")

@frappe.whitelist()
def update_sales_invoice_from_invoice(sales_invoice_name):
    sales_invoice = frappe.get_doc("Sales Invoice", sales_invoice_name)
    
    address = frappe.get_doc("Address", sales_invoice.customer_address)

    if sales_invoice.organo_gestor != address.organo_gestor or sales_invoice.oficina_contable != address.oficina_contable or sales_invoice.unidad_tramitadora != address.unidad_tramitadora or sales_invoice.organo_proponente != address.organo_proponente:   
        frappe.db.sql(""" update `tabSales Invoice` set
            organo_gestor=%s,
            oficina_contable=%s,
            unidad_tramitadora=%s,
            organo_proponente=%s
            where name = %s
        """, (address.organo_gestor, address.oficina_contable, 
            address.unidad_tramitadora, address.organo_proponente, 
            sales_invoice_name), debug=False)
        frappe.clear_cache(doctype="Sales Invoice")
        frappe.msgprint("Registro actualizado: {0}".format(sales_invoice_name))