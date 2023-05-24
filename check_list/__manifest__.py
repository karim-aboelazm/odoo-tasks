# -*- coding: utf-8 -*-
{
    'name': "Employees CheckList",

    'summary': "Employees CheckList",

    'description': "Employees CheckList",

    'author': "Engineer. Karim Mohammed Aboelazm",
    
    'website': "http://www.karimaboelazm.com",
    
    'sequence':-200,
    'category': 'Others',
    'version': '0.1',
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/checklist_employee.xml',  
        'views/checklist_action.xml',  
        'views/checklist_form.xml',  
        'views/checklist_tree.xml',  
        'views/checklist_menu.xml',  
    ],
    # only loaded in demonstration mode
    'demo': [ 'demo/demo.xml',],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}
