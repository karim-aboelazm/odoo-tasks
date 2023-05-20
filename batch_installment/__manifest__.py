# -*- coding: utf-8 -*-
{
    'name': "Batch Installment",

    'summary': "Batch Installment",

    'description': "Batch Installment",
    'sequence':-100,
    'licence':'AGPL-3',
    'author': "Karim Mohammed Aboelazm",
    'website': "http://www.itss.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','fleet','purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/batch_payment.xml',
        'views/fleet_contract.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'batch_installment/static/src/js/*.js',
        ],
        'web.assets_qweb': [
            'batch_installment/static/src/xml/*.xml',
        ],
    },
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}