# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Movement(models.Model):
     _name = 'g2_bank.Movement'
     _description = 'Movement of Account'

     

     name = fields.Char()
     timestamp = fields.Date()
     amount = fields.Monetary()
     balance = fields.Monetary()
     
     Movement_ids=fields.Many2one('g2_bank.Account', string ="Account")
     
     
     
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100