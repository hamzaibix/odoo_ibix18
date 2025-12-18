from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    arabic_name1 = fields.Char(string="Company Arabic Name")
    arabic_address1 = fields.Char(string="Company Arabic Address")
    arabic_address2 = fields.Char(string="Company Arabic Address2")