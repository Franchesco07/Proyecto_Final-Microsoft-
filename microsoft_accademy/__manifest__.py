{
    'name': 'Microsoft Suite - Academia de Certificaciones',
    'version': '1.0',
    'category': 'Administration',
    'summary': 'Control de capacitaciones, asignación de vouchers y registro de exámenes de certificación de Microsoft.',
    'author': 'Franchesco',
    'depends': [
        'base',
        'hr',                
        'microsoft_suite',    
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/microsoft_certification_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}