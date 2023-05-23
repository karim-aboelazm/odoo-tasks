# -*- coding: utf-8 -*-
{
    'name': "HrSalary",

    'summary': "Hr salary task",

    'description': "Hr salary task",

    'author': "Karim Mohammed Aboelazm",
    
    'website': "https://www.itss.com",
    
    'category': 'Uncategorized',
    
    'version': '0.1',

    'depends': ['base','hr','hr_contract'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        
        'views/employee.xml',
        
        'views/contract.xml',
        
        'views/allowance.xml',
        
        'views/deduction.xml',
        
        'views/contract_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}