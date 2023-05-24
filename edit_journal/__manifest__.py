# -*- coding: utf-8 -*-
{
    'name': "Edit Journal",

    'summary': "Edit Journal",

    'description': "Edit Journal",
    'author': "Karim Mohammed Aboelazm",
    'website': "http://www.itss.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/journal.xml',
        'views/payment.xml',
        'views/transient.xml',
        # 'views/settings_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}

