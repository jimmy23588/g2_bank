# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class Account(models.Model):
     _name = 'g2_bank.Account'
     _description = 'Account'
     
     name = fields.Text()
     balance = fields.Monetary(required = true)
     creditLine = fields.Monetary()
     beginBalance = fields.Monetary()
     beginBalanceTimestamp = fields.Datetime()
     typeAccount = fields.Selection(required = true)
     Customer_ids = fields.Many2Many('g2_bank.Customer', string="Customers")
     Movement_id = fields.One2many('g2_bank.Movement', string="Movements")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
