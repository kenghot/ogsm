from odoo import models, fields

class Objective(models.Model):
    _name = 'ogsm.objective'
    _description = 'Objective'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    target_date = fields.Date(string='Target Date')
    achieved = fields.Boolean(string='Achieved')
