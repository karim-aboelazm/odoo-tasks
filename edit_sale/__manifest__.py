# -*- coding: utf-8 -*-
{
    'name': "EditSale",

    'summary': "Edit Sales and Purchase Form",

    'description': "Edit Sales and Purchase Form",

    'author': "Karim Mohammed Aboelazm",
    'website': "https://www.itss.com",
    
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','sale','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_edit.xml',
        'views/purshase_edit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}