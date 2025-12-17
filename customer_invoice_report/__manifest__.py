# -*- coding: utf-8 -*-
{
    'name': "Customer Invoice Report",

    'summary': "Customer Invoice Report",

    'description': "Customer Invoice Report",

    'author': "Syed Hamza Arif",
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','stock'],
    # always loaded
    'data': [
        'template.xml',
        'views/module_report.xml',
    ],
    'css': ['static/src/css/report.css'],
}
