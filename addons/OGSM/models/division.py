from odoo import models, fields

class Division(models.Model):
    _name = 'ogsm.division'
    _description = 'Division'

    code = fields.Char(string='Code', required=True)
    name = fields.Char(string='Name', required=True)
    user_ids = fields.Many2many('res.users', string='Users')
