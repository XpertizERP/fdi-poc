# -*- coding: utf-8 -*-

{
    'name' : 'FDI base',
    'version' : '1.0.0',
    'description': """
FDI base module, will trigger the installation of the necessary module for FDI.
    """,
    'category': 'FDI',
    'author': 'Xpertiz S.A.',
    'website': 'http://www.xpertiz.lu',
    'depends': ['timesheet_grid','FDI_project'],
    'data': [
        'security/FDI_security.xml',
    ],
    'demo': [],
    'qweb': [],
    'application': True,
}
