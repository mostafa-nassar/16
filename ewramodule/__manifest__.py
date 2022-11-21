# -*- coding: utf-8 -*-
{
    'name': "ewramodule",

    'summary': """
        theis is ewra modules contain all ewra logic copy right reserved""",

    'description': """
        theis is ewra modules contain all ewra logic copy right reserved
    """,

    'author': "Ahmed Abd Al Aziz",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','helpdesk','contacts','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        "views/snippest.xml",
        'views/helpdeskticket.xml',
        'views/templates.xml',
        'views/helpdisktemplate.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets':{
        'web.assets_frontend':[
            # "https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,500,500i,700,700i,900,900i|Source+Sans+Pro:300,300i,400,400i,600,600i,700,700i,900,900i&display=swap",
            # 'ewratheme/static/src/scss/style.css',
            'ewramodule/static/src/js/ewra_ticketsubmit.js',
            
            
        ],
        'web.assets_qweb': [
         # 'ewramodule/static/src/xml/helpdisktemplate.xml',
            ],
        },
}
