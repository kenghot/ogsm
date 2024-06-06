from odoo import api, models, fields

class Module(models.Model):
    _inherit = "ir.module.module"

    group_id = fields.Many2one('ir.module.category', string='Group',store = True)