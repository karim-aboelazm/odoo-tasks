# -*- coding: utf-8 -*-

from odoo import models, fields, api



class AccountPayment(models.Model):
    _inherit = 'account.payment'

    bank_free_account = fields.Many2one(related='journal_id.bank_free_accounts', string='Bank Free Account')
    commission_journal = fields.Many2one(related='journal_id.journal', string='Commission Journal')
    commission_amount = fields.Monetary(string='Commission Amount')
    show_create_button = fields.Boolean(string='Show Create Button', default=True)
    def open_commission_entry(self):
        self.ensure_one()
        JournalEntry = self.env['account.move']
         # Check if a commission entry already exists
        existing_entry = JournalEntry.search([
            ('journal_id', '=', self.commission_journal.id),
            ('state', '!=', 'cancel'),
            ('payment_id', '=', self.id)
        ], limit=1)
        
        if existing_entry:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Commission Entry',
                'view_mode': 'form',
                'res_model': 'account.move',
                'res_id': existing_entry.id,
                'target': 'current',
            }
        else:
            move = JournalEntry.create({
                'journal_id': self.commission_journal.id,
                'line_ids': [
                    (0, 0, {
                        "journal_id": self.commission_journal.id,
                        'account_id': self.bank_free_account.id,
                        'debit': self.commission_amount,
                    }),
                    (0, 0, {
                        "journal_id": self.commission_journal.id,
                        'account_id': self.journal_id.default_account_id.id,
                        'credit': self.commission_amount,
                    }),
                ],
            })
            return {
                'type': 'ir.actions.act_window',
                'name': 'Commission Entry',
                'view_mode': 'form',
                'res_model': 'account.move',
                'res_id': move.id,
                'target': 'current',
            }