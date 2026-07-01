{
    'name': 'Microsoft',
    'version': '1.0',
    'summary': 'Gestion y facturacíon de licencias Microsoft y consumo de Azure ',
    'category': 'Sales',
    'author': 'Franchesco',
    'depends': ['base', 'product', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/product_template_views.xml',
        'views/microsoft_subscription_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}