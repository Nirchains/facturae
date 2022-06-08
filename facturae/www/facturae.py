# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals

from frappe.contacts.doctype.address.address import get_default_address

from six import iteritems
from six.moves.urllib.parse import quote, urljoin

import frappe, json
from frappe.model.document import get_controller
from frappe.utils import get_datetime, get_url, nowdate
from frappe.website.router import get_all_page_context_from_doctypes, get_pages

no_cache = 1
#base_template_path = "templates/www/facturae.xml"


def get_context(context):
	"""generate the factura XML"""


	
	context.sales_invoice_name = frappe.local.form_dict.sales_invoice_name

	context.sales_invoice = frappe.get_doc("Sales Invoice", context.sales_invoice_name)
	
	namesplit = context.sales_invoice.name.split("-")
	context.sales_invoice.serie = "{0}-{1}".format(namesplit[0], namesplit[1])
	#context.sales_invoice.number = int(namesplit[2])
	context.sales_invoice.number = context.sales_invoice.name.replace(context.sales_invoice.serie, "")

	context.company = frappe.get_doc("Company", context.sales_invoice.company)
	company_address_name = get_default_address("Company", context.company.name)
	context.company_address = frappe.get_doc("Address", company_address_name)
	context.company_address.country_code = frappe.db.get_value("Country", context.company_address.country, "code")

	context.company.default_bank_account_number = frappe.db.get_value("Bank Account", {"account": context.company.default_bank_account, "company": context.company.name}, "iban")

	context.customer = frappe.get_doc("Customer", context.sales_invoice.customer)
		
	if context.customer.customer_type == "Company":
		context.customer.PersonTypeCode = "J"
	else:
		context.customer.PersonTypeCode = "F"

	customer_address_name = get_default_address("Customer", context.customer.name)
	context.customer_address = frappe.get_doc("Address", customer_address_name)
	context.customer_address.country_code = frappe.db.get_value("Country", context.customer_address.country, "code")