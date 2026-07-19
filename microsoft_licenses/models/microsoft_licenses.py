from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MicrosoftLicense(models.Model):
    # _name define el nombre de la tabla en la base de datos (se convertirá en microsoft_license)
    _name = 'microsoft.license'
    _description = 'Registro de Licencias de Microsoft'
    
    # Campo obligatorio en Odoo para identificar el registro en las búsquedas
    name = fields.Char(string='Clave/ID de Licencia', required=True)
    
    # Selection: Una lista desplegable con opciones predefinidas
    license_type = fields.Selection([
        ('m365_business', 'Microsoft 365 Business Premium'),
        ('m365_enterprise', 'Microsoft 365 Enterprise E5'),
        ('azure_credits', 'Suscripción Azure (Créditos)'),
        ('power_bi', 'Power BI Pro')
    ], string='Tipo de Licencia', required=True, default='m365_business')
    
    # Date: Campo de fecha para el control de renovaciones
    expiration_date = fields.Date(string='Fecha de Expiración')
    
    # Many2one: Relación con otra tabla. Vinculamos la licencia a un Usuario nativo de Odoo
    user_id = fields.Many2one('res.users', string='Usuario Asignado')
    
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('active', 'Activa'),
        ('expired', 'Expirada')
    ], string='Estado', default='draft')

    # --- LÓGICA DE NEGOCIO (PASO A PASO) ---

    # 1. Restricción en Python (@api.constrains):
    # Evita que se guarde una licencia si la fecha de expiración ya pasó.
    @api.constrains('expiration_date')
    def _check_expiration_date(self):
        for record in self:
            if record.expiration_date and record.expiration_date < fields.Date.today():
                raise ValidationError("No puedes registrar o activar una licencia cuya fecha de expiración sea anterior a hoy.")

    # 2. Acción para activar la licencia de forma manual mediante un botón
    def action_activate(self):
        for record in self:
            if not record.user_id:
                raise ValidationError("Debes asignar un usuario a la licencia antes de activarla.")
            record.state = 'active'
