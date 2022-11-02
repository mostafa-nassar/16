# -*- coding: utf-8 -*-
{
    'name': "helpdesk_custom_portal",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','helpdesk','contacts','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/partner.xml',
        'views/helpdesk.xml',
        'views/partner_area_zone_view.xml',
        'views/drinking_watter.xml',
        'views/complain_issue.xml',
        'views/sewage_watter.xml',
        'views/commercial_watter.xml'
        # 'views/quality_type.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'helpdesk_custom_portal/static/css/adminlte.min.css',
            'helpdesk_custom_portal/static/css/style.css',

            'helpdesk_custom_portal/static/js/adminlte.min.js',
            'helpdesk_custom_portal/static/js/inputmask/jquery.inputmask.min.js',
            'helpdesk_custom_portal/static/js/select2/js/select2.min.js',
            'helpdesk_custom_portal/static/js/select2/css/select2.min.css',
            'helpdesk_custom_portal/static/js/select2/css/select2-bootstrap4.min.css',
            'helpdesk_custom_portal/static/js/toastr/toastr.min.css',
            'helpdesk_custom_portal/static/js/toastr/toastr.min.js',
            'helpdesk_custom_portal/static/js/jquery-validation/jquery.validate.min.js',
            'helpdesk_custom_portal/static/js/jquery-validation/additional-methods.min.js',
            'helpdesk_custom_portal/static/js/helpdesk.js',
        ],
    }
}
