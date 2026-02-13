
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Account(models.Model):
     _name = 'g2_bank.account'
     _description = 'Account'
     
     name = fields.Text(string = "Name", required=True)
     balance = fields.Float(string = "Balance")
     creditLine = fields.Float(string = "Credit Line")
     beginBalance = fields.Float(string = "Begin Balance", required=True)
	 #FIXME la fecha tiene valor por defecto la actual y no se permite editar en las vistas.
     beginBalanceTimestamp = fields.Datetime(string = "Date", required=True)
     typeAccount = fields.Selection(
     [
            ('standar', 'Standar'),
            ('credit', 'Credit'),
        ],
        string="Account Type"
    )

  	#FIXME Asocia la cuenta con el usuario que está creando la cuenta cuando esta se cree
     Customers_ids = fields.Many2many('res.users', string="Customers", required=True)
     Movements_ids = fields.One2many('g2_bank.movement', 'account_id', string="Movements")

	#FIXME Añadir constrains que validen que todos los importes son positivos
	
	#FIXME El balance no es editable nunca (comprobarlo en la vista correspondiente) si no que 
	#es igual al beginBalance cuando se crea la cuenta y luego se va actualizando con cada movimiento.
	#FIXME Para lo anterior probablemente necesites redefinir un método 
	#@api.model_create_multi
    #def create(self, vals_list):
        ## lógica antes de crear
    #    records = super().create(vals_list)
        ## lógica después de crear
    #    return records
    
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
        return super(Account, self).unlink()s.One2many('g2_bank.movement', 'account_id', string="Movements")