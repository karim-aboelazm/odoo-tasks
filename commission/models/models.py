# -*- coding: utf-8 -*-

from odoo import models, fields, api


class commission(models.Model):
    _inherit = 'account.journal'
    
    has_commission = fields.Boolean(string='Has Commission', default=False)
    
    bank_free_accounts = fields.Many2one(
        'account.account',
        string='Bank Free Accounts',
        domain ="[('internal_group', '=', 'expense')]"
    )

    journal = fields.Many2one(
        'account.journal',
        string='Journal',
        domain="[('type', '=', 'general')]"
    )
# in jornal advanced page with type bank ---> add bool fields called has_commision to display 
#     - bank_free_accounts field as domain for account type expences
#     - journal field as domain for account type general


'''
in account payment adding 3 field display if journal has_commision and payment_type is send only
    1) bank_free_account mandatory
    2) commission_journal mandatory
    3) commission_amount mandatory
    - adding smart button in header called commission entry include
        * debit account from bank_free_account
        * credit(bank_account) journal commission_journal
'''
    
