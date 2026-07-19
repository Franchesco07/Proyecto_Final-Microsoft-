{
    'name': 'Microsoft Suite',
    'version': '1.0',
    'category': 'Administration',
    'summary': 'Módulo raíz para la administración unificada de activos, licencias y certificaciones Microsoft.',
    'description': """
Módulo Padre (Base)
===================
Este módulo actúa como el núcleo de la Suite Microsoft.
Establece:
- El menú raíz unificado del sistema.
- Los grupos de seguridad globales (Administrador, Soporte Técnico, Alumno).
- Los cimientos de acceso para los submódulos hijos.
    """,
    'author': 'Franchesco',
    'depends': ['base', 'hr','mail'],
    'data': [
        'security/groups.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}