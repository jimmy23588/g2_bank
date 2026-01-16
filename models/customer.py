# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
     _name = 'g2_bank.Customer'
     _description = 'Customer'
     _inherit = 'res.users'

     firstname = fields.Text()
     lastname = fields.Text()
     middleInitial = fields.Text()
     street = fields.Text()
     city = fields.Text()
     state = fields.Text()
     zip = fields.Integer()
     phone = fields.Integer()
     email = fields.Text()
     password = fields.Text()

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
