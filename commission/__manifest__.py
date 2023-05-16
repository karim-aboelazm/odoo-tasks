# -*- coding: utf-8 -*-
{
    'name': "Commission",

    'summary': "Journal Commission",

    'description': "Journal Commission",
    'sequence':-100,
    'licence':'AGPL-3',
    'author': "Karim Mohammed Aboelazm",
    'website': "http://www.itss.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}
