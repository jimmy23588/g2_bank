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
    
     @api.depends('amount', 'account_id')
     def _compute_balance(self):
        for record in self:
            if not record.account_id:
                record.balance = 0.0
                continue

            previous_moves = self.search([
                ('account_id', '=', record.account_id.id),
                ('id', '<', record.id)
            ], order='timestamp desc', limit=1)

            previous_balance = previous_moves.balance if previous_moves else 0.0
            record.balance = previous_balance + record.amount
   
       
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