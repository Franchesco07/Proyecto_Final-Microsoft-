from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MicrosoftCertification(models.Model):
    _name = 'microsoft.certification'
    _description = 'Control de Certificaciones Microsoft'
    # Mostraremos el código del examen y el nombre como identificador principal
    _rec_name = 'display_name'

    certification_code = fields.Char(string='Código de Examen', required=True, placeholder="Ej: AZ-900, PL-300")
    name = fields.Char(string='Nombre de Certificación', required=True, placeholder="Ej: Azure Fundamentals")
    
    # Relación con el empleado que tomará el examen
    employee_id = fields.Many2one('hr.employee', string='Empleado / Alumno', required=True)
    
    voucher_code = fields.Char(string='Código de Voucher', help="Código único para canjear el examen gratuito")
    exam_date = fields.Date(string='Fecha Programada')
    
    # Campo numérico para el puntaje (En certificaciones de Microsoft el rango es de 0 a 1000)
    score = fields.Integer(string='Puntaje Obtenido', default=0)
    
    status = fields.Selection([
        ('registered', 'Registrado / Estudiando'),
        ('passed', 'Aprobado (Certified)'),
        ('failed', 'No Aprobado'),
        ('expired', 'Voucher Expirado')
    ], string='Estado de Certificación', default='registered')

    # Campo calculado dinámicamente para mostrar en la interfaz (Código + Nombre)
    display_name = fields.Char(string='Nombre Completo', compute='_compute_display_name', store=True)

    @api.depends('certification_code', 'name')
    def _compute_display_name(self):
        for record in self:
            if record.certification_code and record.name:
                record.display_name = f"[{record.certification_code}] {record.name}"
            else:
                record.display_name = record.name or record.certification_code or '/'

    # --- LÓGICA DE NEGOCIO ---

    # 1. Restricción en Python (@api.constrains):
    # Validamos que el puntaje no sea un número absurdo. Debe estar entre $0$ y $1000$ puntos.
    @api.constrains('score')
    def _check_score_range(self):
        for record in self:
            if record.score < 0 or record.score > 1000:
                raise ValidationError("El puntaje de certificación de Microsoft debe estar comprendido estrictamente entre 0 y 1000 puntos.")

    # 2. Lógica Automática:
    # Si ingresamos un puntaje, evaluamos de forma inmediata el resultado.
    # En Microsoft, el puntaje mínimo de aprobación (Passing Score) es de 700 puntos.
    @api.onchange('score')
    def _onchange_score_evaluation(self):
        if self.score >= 700:
            self.status = 'passed'
        elif self.score > 0 and self.score < 700:
            self.status = 'failed'