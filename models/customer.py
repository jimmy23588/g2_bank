# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class Customer(models.Model):
     _name = 'g2_bank.Customer'
     _description = 'Customer'
     _inherit = 'res.users'

     
     Accounts_ids = fields.Many2Many('g2_bank.Customer', string="Customers")
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
