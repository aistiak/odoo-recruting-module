{
    'name': 'Beman Recruiting',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Custom recruiting module',
    'description': """
        Custom recruiting module for managing recruitment process
    """,
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'sequence': 1,
    'license': 'LGPL-3',
} 