#-*- coding: utf-8 -*-

from odoo import models, fields, api


class EditJournal(models.Model):
    _inherit = 'account.journal'
    pocket_id = fields.Boolean(string="Pocket Id", default=False)
    
