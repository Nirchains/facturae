frappe.listview_settings['Sales Invoice'].onload = function(list_view) {
		list_view.page.add_menu_item(__("Actualiza datos FACE"), function() {
            const registros = list_view.get_checked_items();
            //console.log(list_view.get_checked_items(true));
            registros.forEach(element => {
                frappe.call({
                    method: "facturae.utils.update_sales_invoice_from_invoice",
                    args: {sales_invoice_name: element.name},
                    callback: function(r) {
                        if(r.message) {
                            
                        }
                        
                    }
                });
            });
			

		});
};
