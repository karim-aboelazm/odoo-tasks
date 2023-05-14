from odoo import models, fields, api

class BatchInternalTransfare(models.Model):
    _name = 'batch.internal.transfare'
    _description = 'Batch Internal Transfare'

    current_date = fields.Date(string='Date', default=fields.Date.context_today, required=True)
    transfer_to = fields.Many2one('account.journal', string='Transfer To',
                                  domain="[('type', 'in', ['bank', 'cash'])]")
    state = fields.Selection([(i,i.title()) for i in ['draft','waiting approve','approved']],'State', default="draft")
    transfer_from = fields.Many2one('account.journal', string='Transfer From',
                                    domain="[('type', 'in', ['bank', 'cash'])]")
    internal_transfer = fields.Boolean(default=True)
    
    payment_lines = fields.One2many('account.payment','payment_id', string='Payment Lines')
    
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft'    , 'waiting approve'),  
                   ('waiting approve', 'approved' )]  
        return (old_state, new_state) in allowed

    def change_state(self, new_state): 
        for bit in self:  
            if bit.is_allowed_transition(bit.state, new_state): 
                bit.state = new_state 
            else:
                continue

    def make_waiting_approve(self):
        self.change_state('waiting approve')

    def make_approved(self):
        self.change_state('approved')
