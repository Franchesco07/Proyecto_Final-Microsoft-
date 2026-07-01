from odoo import models , fields 

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_microsoft_product = fields.Boolean (string='Producto Microsoft', default=False)
    microsoft_type = fields.Selection([
        ('license', 'Licencia fija (M365/Office)'),
        ('consumption', 'Consumo variable (Azure)'),
    ], string='Tipo de producto Microsoft', help='Tipo de producto Microsoft')
    microsoft_sku = fields.Char(string="SKU de Microsoft", help="Identificador único del producto en el Centro de Microsoft")