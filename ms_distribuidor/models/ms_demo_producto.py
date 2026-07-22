from odoo import fields, models


class MsDemoProducto(models.Model):
    _name = 'ms.demo_producto'
    _description = 'Demo o prueba de producto'
    _order = 'fecha_hora desc'

    name = fields.Char(string='Referencia', default='Nuevo')
    cliente_id = fields.Many2one('ms.cliente', string='Cliente')
    producto_id = fields.Many2one('ms.producto', string='Producto')
    vendedor_id = fields.Many2one('ms.vendedor', string='Vendedor')
    fecha_hora = fields.Datetime(string='Fecha y hora', default=fields.Datetime.now)
    duracion_horas = fields.Float(string='Duracion (horas)', default=0.5)
    notas = fields.Text(string='Notas')
    estado = fields.Selection(
        selection=[
            ('borrador', 'Borrador'),
            ('confirmada', 'Confirmada'),
            ('realizada', 'Realizada'),
        ],
        string='Estado',
        default='borrador',
    )

    def action_confirmar(self):
        for demo in self:
            if demo.estado == 'borrador':
                demo.estado = 'confirmada'

    def action_realizada(self):
        for demo in self:
            demo.estado = 'realizada'

    def action_cancelar(self):
        for demo in self:
            demo.estado = 'borrador'
