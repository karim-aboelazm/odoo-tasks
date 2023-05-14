# -*- coding: utf-8 -*-
{
    'name': "BatchInternalTransfare",

    'summary': "Batch Internal Transfare Task",

    'description': "Batch Internal Transfare Task",
    'sequence':-100,
    'author': "Karim Mohammed Aboelazm",
    'website': "http://www.itss.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/batch_internal_transfare_action.xml',
        'views/batch_internal_transfare_form.xml',
        'views/batch_internal_transfare_tree.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}
