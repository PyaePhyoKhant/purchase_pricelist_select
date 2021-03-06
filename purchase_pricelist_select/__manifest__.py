# -*- coding: utf-8 -*-
{
    'name': "Purchase Pricelist Select",

    'summary': """
        Manually select pricelist in purchase form""",

    'description': """
        Manually select pricelist in purchase form. 
        The same pricelist workflow as in sale pricelist. 
        Define purchase pricelist at Purchase/Configuration.
        If product is in purchase pricelist, that product price will be used.
        Otherwise, vendor pricelsit is used. 
    """,

    'author': "Pyae Phyo Khant",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_form_inherit.xml',
        'views/purchase_pricelist_menu.xml',
        'views/purchase_pricelist_views.xml',
    ],
}
