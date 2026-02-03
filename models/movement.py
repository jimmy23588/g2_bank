# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Movement(models.Model):
     _name = 'g2_bank.movement'
     _description = 'Movement of Account'
    
     name = fields.Text(string = "Description", required=True)
     timestamp = fields.Date(string = "TimeStamp", required = True, default=fields.Datetime.today)
     amount = fields.Float(string = "Amount", default=0.0)
     balance = fields.Float(string = "Balance", default=0.0)
    
     account_id = fields.Many2one('g2_bank.account', string="Account")
     
     
     @api.constrains('amount', 'name', 'account_id') 
    def _validationAmountError(self): 
        for record in self: 
            #amount sea positivo 
            if record.amount == 0: 
                #else
                raise ValidationError("The amount cannot be zero.") 
       
    # @api.constrains('date')
     #def _check_date(self):
      #   for record in self:
       #      if record.date and record.date in fields.Date.today:
        #         raise ValidateError("date is error: ")
          
         #     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100