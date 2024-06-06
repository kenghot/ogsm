
from odoo import api, models, fields

class Partner(models.Model):

    _inherit = "res.partner"

    province = fields.Many2one('ggg.lov',string='จังหวัด',store=True,domain=[('group.group_code','=','province'),('isActive','=',True)])
    district = fields.Many2one('ggg.lov',string='เขต',store=True)
    sub_district = fields.Many2one('ggg.lov',string='แขวง',store=True)
  
    @api.onchange("province")
    def on_province_changed(self):
        self.district = False
        self.sub_district = False

    @api.onchange("district")
    def on_district_changed(self):
        self.sub_district = False
