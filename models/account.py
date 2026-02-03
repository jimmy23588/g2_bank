
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Account(models.Model):
     _name = 'g2_bank.account'
     _description = 'Account'
     
     name = fields.Text(string = "Name", required=True)
     balance = fields.Float(string = "Balance", required=True)
     creditLine = fields.Float(string = "Credit Line")
     beginBalance = fields.Float(string = "Begin Balance")
     beginBalanceTimestamp = fields.Datetime(string = "Date")
     typeAccount = fields.Selection(
     [
            ('standar', 'Standar'),
            ('credit', 'Credit'),
        ],
        string="Account Type"
    )
    
     Customers_ids = fields.Many2many('res.users', string="Customers")
     Movements_ids = fields.One2many('g2_bank.movement', 'account_id', string="Movements")

     
def write(self, vals):
        for record in self:
            if record.typeAccount != 'credit':
                # Solo editable si es credit
                not_editable = [f for f in vals if f in ('creditLine')]
                if not_editable:
                    raise ValidationError(
                        "Credit Line es editable si la cuenta es de tipo CREDIT."
                    )
        return super(Account, self).write(vals)
    