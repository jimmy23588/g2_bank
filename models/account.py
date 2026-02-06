
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Account(models.Model):
     _name = 'g2_bank.account'
     _description = 'Account'
     
     name = fields.Text(string = "Name", required=True)
     balance = fields.Float(string = "Balance")
     creditLine = fields.Float(string = "Credit Line")
     beginBalance = fields.Float(string = "Begin Balance", required=True)
     beginBalanceTimestamp = fields.Datetime(string = "Date", required=True)
     typeAccount = fields.Selection(
     [
            ('standar', 'Standar'),
            ('credit', 'Credit'),
        ],
        string="Account Type"
    )
    
     Customers_ids = fields.Many2many('res.users', string="Customers", required=True)
     Movements_ids = fields.One2many('g2_bank.movement', 'account_id', string="Movements")

    
    @api.constrains('creditLine', 'typeAccount')
    def _established_credit_line_only_credit(self):
        for record in self:
            if record.typeAccount != 'credit' and record.creditLine:
                raise ValidationError(
                    "Credit Line solo puede modificarse si la cuenta es de tipo CREDIT."
                )
def unlink(self):
        for account in self:
            if account.Movements_ids:
                raise UserError(
                    "No se puede borrar una cuenta que tenga movimientos asociados."
                )
        return super(Account, self).unlink()