# -*- coding: utf-8 -*-
{
    'name': "Employees Document",

    'summary': "Employees Document",

    'description': "Employees Document",

    'author': "Engineer. Karim Mohammed Aboelazm",
    
    'website': "http://www.karimaboelazm.com",
    
    'sequence':-200,
    'category': 'Others',
    'version': '0.1',
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/document_action.xml',  
        'views/document_form.xml',  
        'views/document_tree.xml',  
        'views/document_menu.xml',  
    ],
    # only loaded in demonstration mode
    'demo': [ 'demo/demo.xml',],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}
