# -*- coding: utf-8 -*-
{
    'name': "Arab Council for children and Development",

    'summary': "Arab Council for children and Development",

    'description': "Arab Council for children and Development",

    'author': "Engineer. Karim Mohammed Aboelazm",
    
    'website': "http://www.karimaboelazm.com",
    
    'sequence':-200,
    'category': 'Others',
    'version': '0.1',
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        
       
        # Experts all Views
        'views/expert_window_action.xml',
        'views/expert_form_view.xml',
        'views/expert_tree_view.xml',
        
        # Skills all Views
        'views/skills_window_action.xml',
        'views/skills_form_view.xml',
        'views/skills_tree_view.xml',
        
        # company all Views
        'views/company_window_action.xml',
        'views/company_form_view.xml',
        'views/company_tree_view.xml',
        
        # work field all Views
        'views/work_field_window_action.xml',
        'views/work_field_form_view.xml',
        'views/work_field_tree_view.xml',
      
        # work field all Views
        'views/work_history_window_action.xml',
        'views/work_history_form_view.xml',
        'views/work_history_tree_view.xml',
       
        # Company type field all Views
        'views/company_type_window_action.xml',
        'views/company_type_form_view.xml',
        'views/company_type_tree_view.xml',
       
        # Menu Items Views
        'views/main_menu_item.xml',
         
    ],
    # only loaded in demonstration mode
    'demo': [ 'demo/demo.xml',],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}
