# -*- coding: utf-8 -*-
 from odoo import models ,fields,api
 
 #import models,fields,api


 class g2_bank(models.Model):
    #_name = 'g2_bank.g2_bank'
   # _description = 'g2_bank.g2_bank'

  #  name = fields.Char()
   #  value = fields.Integer()
   #  value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()

     @api.depends('value')
     def _value_pc(self):
         for record in self:
             record.value2 = float(record.value) / 100
