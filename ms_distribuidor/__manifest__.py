{
    'name': 'Microsoft Store - Distribuidor',
    'version': '18.0.1.0.0',
    'summary': 'Gestion de productos, clientes, ventas y demos para distribuidor Microsoft (Ecuador)',
    'description': """
Modulo 100% personalizado para una tienda distribuidora de productos Microsoft.
No hereda ni integra modelos predefinidos de Odoo (product, hr, partner, sale, stock, account, mail).
IVA fijo del 15% calculado en Python, sin modulo de contabilidad.
""",
    'author': 'Franchesco07',
    'category': 'Sales',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/ms_venta_sequence.xml',
        'views/ms_producto_views.xml',
        'views/ms_cliente_views.xml',
        'views/ms_vendedor_views.xml',
        'views/ms_demo_producto_views.xml',
        'views/ms_venta_views.xml',
        'views/menus.xml',
        'data/ms_datos_iniciales.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
