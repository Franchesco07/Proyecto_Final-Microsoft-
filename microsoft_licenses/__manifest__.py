{
    'name': 'Microsoft Suite - Gestión de Licencias',
    'version': '1.0',
    'category': 'Administration',
    'summary': 'Control, asignación y auditoría de licencias de software de Microsoft (M365, Azure).',
    'author': 'Franchesco',
    'depends': ['base','microsoft_suite',],
    'data': [
        'security/ir.model.access.csv',
        'views/microsoft_license_views.xml',
    ],
    'installable': True,
    'application': False,  
    'auto_install': False,
    'license': 'LGPL-3',
}

