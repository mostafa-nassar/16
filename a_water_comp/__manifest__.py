# -*- coding: utf-8 -*-
{
    'name': "جهاز تنظيم مياه الشرب ",

    'summary': """
        جهاز تنظيم مياه الشرب والصرف الصحي وحماية المستهلك""",

    'description': """
جهاز تنظيم مياه الشرب والصرف الصحي وحماية المستهلك
    """,

    'author': "omar rady",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'sequence': '-100',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/view.xml',
        'views/menu.xml',
        'views/perating_surplus.xml',
        'views/Electricity.xml',
        'views/Cost_per_cubic.xml',
        'views/water_statement.xml',
        'views/replacement.xml',
        'views/staff_number.xml',
        'views/collection_table.xml',
        'views/investment_projects.xml',
        'views/org_type.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
