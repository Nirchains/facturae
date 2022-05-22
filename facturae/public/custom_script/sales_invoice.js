console.log("funciona1");
frappe.ui.form.on('Sales Invoice', {
	onload: function(frm) {
		//frappe.breadcrumbs.add("Metalgrafica", "Batch");
        console.log("funciona2");
		msgprint("funciona");
	}
});
