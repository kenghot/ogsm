{
    'name': 'OGSM',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'OGSM Management',
    'description': """
        This module manages OGSM (Objectives, Goals, Strategies, and Measures).
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
         'security/ir.model.access.csv',
        'security/ir.rule.xml',
        'views/objective_view.xml',
        'views/division_view.xml',
        'views/res_users_view.xml',
        'views/menu_view.xml',
    
    ],
    'installable': True,
    'application': True,
}
