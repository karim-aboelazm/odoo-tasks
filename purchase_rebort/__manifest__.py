# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Report",

    'summary': "Purchase Order Report",

    'description': "Purchase Order Report",

    'author': "Engineer. Karim Mohammed Aboelazm",
    
    'website': "http://www.karimaboelazm.com",
    
    'sequence':-200,
    'category': 'Others',
    'version': '0.1',
    'depends': ['base','hr','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/purchase_order_report.xml',  
    ],
    # only loaded in demonstration mode
    'demo': [ 'demo/demo.xml',],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}
