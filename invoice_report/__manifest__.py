# -*- coding: utf-8 -*-
{
    'name': "Invoice report",

    'summary': "Invoice report",

    'description': "Invoice report",

    'author': "Engineer. Karim Mohammed Aboelazm",
    
    'website': "http://www.karimaboelazm.com",
    
    'sequence':-300,
    'category': 'Others',
    'version': '0.1',
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/new_report.xml',  
          
    ],
    # only loaded in demonstration mode
    'demo': [ 'demo/demo.xml',],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}
