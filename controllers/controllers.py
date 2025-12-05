# -*- coding: utf-8 -*-
# from odoo import http


# class G2Bank(http.Controller):
#     @http.route('/g2_bank/g2_bank', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/g2_bank/g2_bank/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('g2_bank.listing', {
#             'root': '/g2_bank/g2_bank',
#             'objects': http.request.env['g2_bank.g2_bank'].search([]),
#         })

#     @http.route('/g2_bank/g2_bank/objects/<model("g2_bank.g2_bank"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('g2_bank.object', {
#             'object': obj
#         })
