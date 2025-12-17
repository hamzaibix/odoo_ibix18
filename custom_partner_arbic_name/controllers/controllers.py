# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPartnerArbicName(http.Controller):
#     @http.route('/custom_partner_arbic_name/custom_partner_arbic_name', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_partner_arbic_name/custom_partner_arbic_name/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_partner_arbic_name.listing', {
#             'root': '/custom_partner_arbic_name/custom_partner_arbic_name',
#             'objects': http.request.env['custom_partner_arbic_name.custom_partner_arbic_name'].search([]),
#         })

#     @http.route('/custom_partner_arbic_name/custom_partner_arbic_name/objects/<model("custom_partner_arbic_name.custom_partner_arbic_name"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_partner_arbic_name.object', {
#             'object': obj
#         })

