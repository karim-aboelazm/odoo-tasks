# -*- coding: utf-8 -*-
{
    'name': "Attendance",

    'summary': "Attendance",

    'description': "Attendance",
    'sequence':-100,
    'author': "Karim Mohammed Aboelazm",
    'website': "http://www.itss.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_attendance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
        'views/attendance.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable'   : True,
    'auto_install'  : False,
    'application'   : True,
}
