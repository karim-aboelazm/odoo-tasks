# -*- coding: utf-8 -*-
{
    'name': "New Fields",

    'summary': "New Fields",

    'description': "New Fields",

    'author': "Engineer. Karim Mohammed Aboelazm",
    
    'website': "http://www.karimaboelazm.com",
    
    'sequence':-200,
    'category': 'Others',
    'version': '0.1',
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        
        'views/partners.xml', 
         
        'views/property_wa.xml',  
        'views/property_form.xml',  
        'views/property_tree.xml',  
        'views/property_search.xml',
        
        'views/property_product_wa.xml',    
        'views/property_product_form.xml',  
        'views/property_product_tree.xml',  
        'views/property_product_search.xml', 
         
        'views/property_reservation_wa.xml',    
        'views/property_reservation_form.xml',  
        'views/property_reservation_tree.xml',  
        'views/property_reservation_search.xml',
          
        'views/property_contract_wa.xml',    
        'views/property_contract_form.xml',  
        'views/property_contract_tree.xml',  
        'views/property_contract_search.xml',
          
        'views/property_menu.xml',  
    ],
    # only loaded in demonstration mode
    'demo': [ 'demo/demo.xml',],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}
