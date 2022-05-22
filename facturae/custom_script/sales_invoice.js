cur_frm.add_fetch('customer_address', 'metodo_envio', 'metodo_envio');
cur_frm.add_fetch('customer_address', 'organo_gestor', 'organo_gestor');
cur_frm.add_fetch('customer_address', 'unidad_tramitadora', 'unidad_tramitadora');
cur_frm.add_fetch('customer_address', 'oficina_contable', 'oficina_contable');
cur_frm.add_fetch('customer_address', 'organo_proponente', 'organo_proponente');

frappe.ui.form.on('Sales Invoice', {
	refresh: function(frm) {
		frm.set_value("tc_name", "IVA 0");
		frm.refresh_fields();
	}
});
