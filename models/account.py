# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Account(models.Model):
     _name = 'g2_bank.account'
     _description = 'Account'
     
     name = fields.Text()
     balance = fields.Float(required=True)
     creditLine = fields.Float()
     beginBalance = fields.Float()
     beginBalanceTimestamp = fields.Datetime()
     typeAccount = fields.Selection(
     [
            ('standar', 'Standar'),
            ('credit', 'Credit'),
        ],
        string="Account Type"
    )
    
     Customer_ids = fields.Many2many('g2_bank.customer', string="Customers")
     Movement_id = fields.One2many('g2_bank.movement', string="Movements")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
