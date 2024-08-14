from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'


    case_no = fields.Char(string='Case No')