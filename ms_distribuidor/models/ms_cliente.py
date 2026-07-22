from odoo import fields, models


class MsCliente(models.Model):
    _name = 'ms.cliente'
    _description = 'Cliente de la tienda'
    _order = 'name'

    name = fields.Char(string='Nombre', required=True)
    tipo_identificacion = fields.Selection(
        selection=[
            ('cedula', 'Cedula'),
            ('ruc', 'RUC'),
            ('pasaporte', 'Pasaporte'),
        ],
        string='Tipo de identificacion',
        default='cedula',
    )
    identificacion = fields.Char(string='Identificacion')
    telefono = fields.Char(string='Telefono')
    email = fields.Char(string='Correo')
    direccion = fields.Char(string='Direccion')
    ciudad = fields.Char(string='Ciudad')
