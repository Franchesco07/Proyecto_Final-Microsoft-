from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MicrosoftAsset(models.Model):
    _name = 'microsoft.asset'
    _description = 'Control de Activos Microsoft Surface'
    # Usaremos el número de serie como identificador principal del registro
    _rec_name = 'serial_number' 

    serial_number = fields.Char(string='Número de Serie', required=True)
    
    model = fields.Selection([
        ('surface_pro', 'Microsoft Surface Pro'),
        ('surface_laptop', 'Microsoft Surface Laptop'),
        ('surface_studio', 'Microsoft Surface Studio Go'),
        ('surface_hub', 'Microsoft Surface Hub')
    ], string='Modelo de Dispositivo', required=True, default='surface_pro')
    
    # Relación Many2one con el modelo nativo de empleados de Odoo (hr.employee)
    employee_id = fields.Many2one('hr.employee', string='Empleado Responsable')
    
    warranty_end = fields.Date(string='Fin de Garantía')
    
    status = fields.Selection([
        ('available', 'Disponible'),
        ('assigned', 'Asignado'),
        ('repair', 'En Servicio Técnico'),
        ('scrapped', 'De Baja / Scrap')
    ], string='Estado del Equipo', default='available')

    # --- LÓGICA DE NEGOCIO ---

    # 1. Restricción para evitar números de serie duplicados
    _sql_constraints = [
        ('uniq_serial_number', 'unique(serial_number)', '¡El número de serie ingresado ya está registrado en el sistema!')
    ]

    # 2. Lógica automática (@api.onchange):
    # Si seleccionamos un empleado, el estado del equipo debe cambiar automáticamente a "Asignado".
    # Si quitamos el empleado, debe volver a estar "Disponible".
    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        if self.employee_id:
            self.status = 'assigned'
        else:
            self.status = 'available'