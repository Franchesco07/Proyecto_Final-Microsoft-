from odoo import fields, models


class MsVendedor(models.Model):
    _name = 'ms.vendedor'
    _description = 'Vendedor de la tienda'
    _order = 'name'

    name = fields.Char(string='Nombre', required=True)
    correo = fields.Char(string='Correo')
    telefono = fields.Char(string='Telefono')
    puesto = fields.Char(string='Puesto')
