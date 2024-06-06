# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class GGGLOV(models.Model):
    _name = "ggg.lov"
    _description = "List of Value"

    name = fields.Char(string="Name")
    code = fields.Char(string="LOV Code")
    group = fields.Many2one("ggg.lov.group")
    parent = fields.Many2one("ggg.lov")
    isActive = fields.Boolean(default=True)
