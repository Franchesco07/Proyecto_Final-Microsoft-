from odoo import api, fields, models

from .ms_producto import IVA_TARIFA


class MsVenta(models.Model):
    _name = 'ms.venta'
    _description = 'Venta de producto Microsoft'
    _order = 'fecha desc, name desc'

    name = fields.Char(string='Referencia', required=True, copy=False,
                       readonly=True, default='Nuevo')
    cliente_id = fields.Many2one('ms.cliente', string='Cliente', required=True)
    producto_id = fields.Many2one('ms.producto', string='Producto', required=True)
    vendedor_id = fields.Many2one('ms.vendedor', string='Vendedor', required=True)
    fecha = fields.Date(string='Fecha', default=fields.Date.context_today)
    precio_base = fields.Float(string='Precio base', compute='_compute_importes', store=True)
    iva_valor = fields.Float(string='IVA (15%)', compute='_compute_importes', store=True)
    total = fields.Float(string='Total', compute='_compute_importes', store=True)
    estado = fields.Selection(
        selection=[
            ('cotizacion', 'Cotizacion'),
            ('confirmada', 'Confirmada'),
            ('facturada', 'Facturada'),
        ],
        string='Estado',
        default='cotizacion',
    )

    @api.depends('producto_id', 'producto_id.precio_base')
    def _compute_importes(self):
        for venta in self:
            venta.precio_base = venta.producto_id.precio_base
            venta.iva_valor = venta.precio_base * IVA_TARIFA
            venta.total = venta.precio_base + venta.iva_valor

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == 'Nuevo':
                vals['name'] = self.env['ir.sequence'].next_by_code('ms.venta') or 'Nuevo'
        return super().create(vals_list)

    def action_confirmar(self):
        for venta in self:
            venta.estado = 'confirmada'

    def action_facturar(self):
        for venta in self:
            venta.estado = 'facturada'

    def action_volver_cotizacion(self):
        for venta in self:
            venta.estado = 'cotizacion'
