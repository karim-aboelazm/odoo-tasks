#-*- coding: utf-8 -*-

from odoo import models, fields, api


class EditPayment(models.Model):
    _inherit = ['account.payment']
    is_bank = fields.Boolean(compute="_get_journal_type")
    new_date = fields.Date(string='New Date', required=True)
    
    @api.depends('journal_id')
    def _get_journal_type(self):
        if self.journal_id.type == 'bank':
            self.is_bank = True
        else:
            self.is_bank = False
