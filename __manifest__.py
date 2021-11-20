# -*- coding: utf-8 -*-
{
    'name': "Sistem Poin App",
    'summary': 'Sistem poin karyawan perusahaan.',
    'description': 'Module Odoo untuk menyimpan dan menampilkan poin karyawan pada perusahaan.',
    'sequence': -100,
    'author': "AntiKeosKeos",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/menus.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
