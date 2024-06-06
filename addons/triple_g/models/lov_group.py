# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class GGGLOVGroup(models.Model):
    _name = "ggg.lov.group"
    _description = "Group of List of Value"

    name = fields.Char(string="Name")
    group_code = fields.Char(string="LOV Group Code")



