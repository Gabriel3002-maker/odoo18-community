# -*- coding: utf-8 -*-
{
    'name': "EcuaRanch",

    'summary': "Adminstrar Ganaderia",

    'description': """Adminstrar Ganaderia  """,

    'author': "Ecuabyte Innovations",
    'website': "https://ecuabyte-innovations.duckdns.org",
    'category': 'Inventory',
    'version': '0.1',

    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/animals_views.xml',
        'views/action_animals.xml',
        'views/animals_menu.xml',
    ],
    'installable': True,
    'application': True
}

