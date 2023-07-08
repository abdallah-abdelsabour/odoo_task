# -*- coding: utf-8 -*-
{
    'name': "Purchase Request Cycle Solution",

    'summary': """
        You are required to create a module that integrates with Odoo purchase module. The module will provide functionality for requesting purchase orders and approving them before purchase orders are created. 
""",

    'description': """
        You are required to create a module that integrates with Odoo purchase module. The module will provide functionality for requesting purchase orders and approving them before purchase orders are created. 

    """,

    'author': "abdallah Abdelsabour",
    'website': "https://www.linkedin.com/in/abdallah-abdelsabour/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','uom'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order.xml',
        'views/purchase_request_views.xml',
        'views/purchase_order_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
