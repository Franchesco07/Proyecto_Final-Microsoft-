from odoo import models, fields, api

class MicrosoftSubscription(models.Model):
    _name = 'microsoft.subscription'
    _description = 'Subscripciones de Clientes Microsoft'
    order = 'name desc'

    name = fields.Char(string="Número de subscripción", required=True, copy=False, readonly=True, index=True, default=lambda self: ('Nuevo'))
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True, domain="[('customer_rank', '>', 0)]")
    product_id = fields.Many2one('product.product', string='Producto/Servicio', required=True, domain="[('is_microsoft_product', '=', True)]")
    quantity = fields.Integer(string='Cantidad de Licencias / Asientos', required=True, default=1)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('active', 'Activa'),
        ('suspended', 'Suspendida'),
    ], string='Estado', default='draft',tracking=True)
    current_consumption = fields.Float(string='Consumo Azure dek Mes ($)', default=0.0, help='Consumo de Azure del mes en curso, calculado automáticamente a partir de la facturación')

    @api.model
    def create(self, vals):
        if vals.get('name', ('Nuevo')) == ('Nuevo'):
            vals['name'] = self.env['ir.sequence'].next_by_code('microsoft.subscription') or ('Nuevo')
        result = super(MicrosoftSubscription, self).create(vals)
        return result