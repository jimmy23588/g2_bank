
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Account(models.Model):
     _name = 'g2_bank.account'
     _description = 'Account'
     #Obtiene de res.currency la moneda Campo relacional Mejora respecto al codigo anterior
     currency_id = fields.Many2one('res.currency', string='Currency', required=True, default=lambda self: self.env.company.currency_id)
     name = fields.Text(string = "Name", required=True)
     balance = fields.Monetary(string="Balance", currency_field='currency_id', compute='_compute_balance', store=True)
     creditLine = fields.Monetary(string="Credit Line", currency_field='currency_id')
     beginBalance = fields.Monetary(string="Begin Balance", currency_field='currency_id', required=True)
	 #FIXME la fecha tiene valor por defecto la actual y no se permite editar en las vistas.
     beginBalanceTimestamp = fields.Datetime(string="Begin Balance Timestamp", default=fields.Datetime.now, readonly=True)
     typeAccount = fields.Selection(
     [
            ('standar', 'Standar'),
            ('credit', 'Credit'),
        ],
        string="Account Type", required=True)

  	#FIXME Asocia la cuenta con el usuario que está creando la cuenta cuando esta se cree
     Customers_ids = fields.Many2many('res.users', string="Customers", required=True, default=lambda self: [(6, 0, [self.env.user.id])])
     Movements_ids = fields.One2many('g2_bank.movement', 'account_id', string="Movements")

	#FIXME Añadir constrains que validen que todos los importes son positivos
     @api.constrains('creditLine', 'balance', 'beginBalance')
     def _check_no_negative_amounts(self):
        for record in self:
            if record.creditLine < 0:
                raise ValidationError("La línea de crédito no puede ser negativa.")
            if record.balance < 0:
                raise ValidationError("El balance no puede ser negativo.")
            if record.beginBalance < 0:
                raise ValidationError("El balance inicial no puede ser negativo.")
	#FIXME El balance no es editable nunca (comprobarlo en la vista correspondiente) si no que 
	#es igual al beginBalance cuando se crea la cuenta y luego se va actualizando con cada movimiento.
	#FIXME Para lo anterior probablemente necesites redefinir un método 
	#@api.model_create_multi
    #def create(self, vals_list):
        ## lógica antes de crear
    #    records = super().create(vals_list)
        ## lógica después de crear
    #    return records
     @api.depends('beginBalance', 'Movements_ids.amount')
     def _compute_balance(self):
        for record in self:
            record.balance = record.beginBalance + sum(m.amount for m in record.Movements_ids)
     #En vez de modificar create y con ayuda de mi compañero este constrains 
     # asigna al balance el beginbalance y despues suma la cantidad que hay en 
     # cada movimiento 
     @api.constrains('creditLine', 'typeAccount')
     def _established_credit_line_only_credit(self):
        for record in self:
            if record.typeAccount != 'credit' and record.creditLine:
                raise ValidationError(
                    "Credit Line solo puede modificarse si la cuenta es de tipo CREDIT."
                )

#FIXME Sangrado o tabulación y verifica que no se pueden borrar las cuentas con movimientos.
     def unlink(self):
        for account in self:
            if account.Movements_ids:
                raise UserError(
                    "No se puede borrar una cuenta que tenga movimientos asociados."
                )
        return super(Account, self).unlink()