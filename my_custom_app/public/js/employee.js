frappe.ui.form.on('Employee', {
    refresh: function(frm) {
        frm.add_custom_button('CI/CD Test Button', () => {
            frappe.msgprint('🎉 CI/CD is working perfectly!');
        });
    }
});

