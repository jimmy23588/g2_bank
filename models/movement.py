# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Movement(models.Model):
     _name = 'g2_bank.movement'
     _description = 'Movement of Account'
    
     name = fields.Text(string = "Description", required=True)
     timestamp = fields.Date(string = "TimeStamp", required = True, default=fields.Datetime.now)
     amount = fields.Float(string = "Amount", default=0.0)
     balance = fields.Float(string = "Balance", default=0.0)
    
     account_id = fields.Many2one('g2_bank.account', string="Account")
     
     
     
     
       
     

     
   
     
     
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100