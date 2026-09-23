{
    'name': 'Hide User Wise Any Menu',
    'version': '19.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'This Module Helps To Hide User Wise Any Menu items.',
    'description': """This module provides functionality to hide or restrict menu 
    items on a per-user basis in Odoo.
    With this feature, administrators can manage which menus each user is allowed 
    to see. It ensures that users only have access to the relevant parts of the system,
     improving both security and usability.""",
    'author': 'Marutiverse',
    'company': 'Marutiverse',
    'maintainer': 'Marutiverse',
    "support": "support.marutiverse@gmail.com",
    'depends': ['base'],
    'data': [
        'views/res_users_views.xml',
        'views/ir_ui_menu_views.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
