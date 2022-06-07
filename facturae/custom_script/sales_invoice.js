cur_frm.add_fetch('customer_address', 'metodo_envio', 'metodo_envio');
cur_frm.add_fetch('customer_address', 'organo_gestor', 'organo_gestor');
cur_frm.add_fetch('customer_address', 'unidad_tramitadora', 'unidad_tramitadora');
cur_frm.add_fetch('customer_address', 'oficina_contable', 'oficina_contable');
cur_frm.add_fetch('customer_address', 'organo_proponente', 'organo_proponente');

frappe.ui.form.on('Sales Invoice', {
	refresh: function(frm) {
		if (frm.doc.docstatus > 0) {
			frm.add_custom_button(__("Cliente"), function() {
			  frappe.route_options = {
				voucher_no: me.frm.doc.name,
				from_date: me.frm.doc.posting_date,
				to_date: moment(me.frm.doc.modified).format("YYYY-MM-DD"),
				company: me.frm.doc.company,
				group_by: "Group by Voucher (Consolidated)",
				show_cancelled_entries: me.frm.doc.docstatus === 2
			  };
			  frappe.set_route("query-report", "General Ledger");
			}, __("View"));
		  }
		if (frm.doc.metodo_envio == "FACE") {
			frm.add_custom_button(__("Generar FACTURAe"), function() {
				var host = window.location.protocol + "//" + window.location.host;
				var url = host + "/facturae/" + frm.doc.name;
				window.open(url);
			}, __('Create'));	
		}

		frm.add_custom_button(__("Enviar factura"), function() {
			frm.trigger("enviar_factura");
		}, __('Create'));	

		//frm.set_value("tc_name", "IVA 0");
		//frm.refresh_fields();
		frm.set_value("payment_terms_template", "Transferencia");
		frm.refresh_fields();
	},

	enviar_factura: function(frm){
		localStorage.removeItem(frm.doctype + frm.docname);
		var d;	
		var args = {
			doc: frm.doc,
			frm: frm,
			sender: "tesoreria@cnde.es",
			subject: __("Cuota miembro CNDE") + ': ' + frm.docname,
			recipients: frm.doc.email || frm.doc.email_id || frm.doc.contact_email,
			attach_document_print: true,
			message: "",
			email_template: "Cuota miembro CNDE",
			real_name: frm.doc.real_name || frm.doc.contact_display || frm.doc.contact_name
		}
		d = new frappe.views.CommunicationComposer(args);
		d.delete_saved_draft();
		d.txt = "1"; //Para borrar el mensaje anterior guardado
		d.dialog.fields_dict.email_template.set_value(d.email_template || '');
				
		return d;
	},

	actualiza_datos: function(frm) {
		frappe.call({
			method: "facturae.utils.update_sales_invoice_from_invoice",
			args: {
				sales_invoice_name: frm.doc.name
			},
			callback: function(r) {
				frm.reload_doc();
			}
		});
	}
	
});
