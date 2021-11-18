# -*- coding: utf-8 -*-
{
    'name': "Sistem Poin App",
    'summary': 'Sistem poin karyawan perusahaan.',
    'description': 'Module Odoo untuk menyimpan dan menampilkan poin karyawan pada perusahaan.',
    'sequence': -100,
    'author': "Kelompok K03-G02",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cats_menus.xml',
        'views/cats_trees.xml',
        'views/cats_forms.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
