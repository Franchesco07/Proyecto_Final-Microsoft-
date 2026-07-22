from odoo import api, fields, models

# IVA vigente en Ecuador para productos tecnologicos. Los productos Microsoft
# (Surface, Xbox, software, accesorios) no estan gravados con ICE: ese impuesto
# aplica unicamente a vehiculos, alcohol y tabaco.
IVA_TARIFA = 0.15


class MsProducto(models.Model):
    _name = 'ms.producto'
    _description = 'Producto Microsoft'
    _order = 'linea, name'

    name = fields.Char(string='Modelo', required=True)
    linea = fields.Selection(
        selection=[
            ('surface', 'Surface'),
            ('xbox', 'Xbox'),
            ('windows', 'Windows'),
            ('office', 'Office'),
            ('accesorio', 'Accesorio'),
        ],
        string='Linea',
        required=True,
    )
    categoria = fields.Selection(
        selection=[
            ('dispositivo', 'Dispositivo'),
            ('software', 'Software'),
            ('consola', 'Consola'),
            ('accesorio', 'Accesorio'),
        ],
        string='Categoria',
        default='dispositivo',
    )
    version_edicion = fields.Char(string='Version / Edicion')
    anio_lanzamiento = fields.Integer(string='Anio de lanzamiento')
    color = fields.Char(string='Color')
    especificaciones = fields.Text(string='Especificaciones')
    tipo_licencia = fields.Selection(
        selection=[
            ('perpetua', 'Perpetua'),
            ('suscripcion', 'Suscripcion'),
            ('no_aplica', 'No aplica'),
        ],
        string='Tipo de licencia',
        default='no_aplica',
    )
    precio_base = fields.Float(string='Precio base', required=True)
    iva_valor = fields.Float(string='IVA (15%)', compute='_compute_impuestos', store=True)
    precio_final = fields.Float(string='Precio final', compute='_compute_impuestos', store=True)
    estado = fields.Selection(
        selection=[
            ('disponible', 'Disponible'),
            ('reservado', 'Reservado'),
            ('agotado', 'Agotado'),
        ],
        string='Estado',
        default='disponible',
    )

    @api.depends('precio_base')
    def _compute_impuestos(self):
        for producto in self:
            producto.iva_valor = producto.precio_base * IVA_TARIFA
            producto.precio_final = producto.precio_base + producto.iva_valor
