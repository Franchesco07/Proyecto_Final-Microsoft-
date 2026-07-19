{
    'name': 'Microsoft Suite - Control de Activos Surface',
    'version': '1.0',
    'category': 'Administration',
    'summary': 'Control del ciclo de vida de hardware Microsoft Surface y asignación a empleados.',
    'author': 'Tu Nombre / Universidad',
    'depends': [
        'base',
        'hr',                 
        'microsoft_suite',    
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/microsoft_asset_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}