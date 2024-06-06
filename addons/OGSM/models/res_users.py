from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    full_name = fields.Char(string='Full Name')
