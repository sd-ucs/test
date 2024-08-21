from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class patient(models.Model):
    _name = 'patient'

    name = fields.Char()
    case_no = fields.Integer()
    date = fields.Datetime()
    is_active = fields.Boolean()
    description = fields.Char()
    patient_id = fields.Many2one('hospital')

