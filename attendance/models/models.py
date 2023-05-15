# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class Attendance(models.Model):
    _name = 'attendance.attendance'

    sequence = fields.Char(string='Sequence', required=True,readonly=True, default=lambda self: _('New'))
    emp_name = fields.Many2one("hr.employee")
    current_date = fields.Date(string='Date', default=fields.Date.context_today, required=True)
    attend_type = fields.Selection(
        selection=[('check-in', 'Check-In'), ('check-out', 'Check-Out'), ('both', 'Both')],
        string='Type'
    )
    state = fields.Selection(selection=[(i,i.title()) for i in ['draft','waiting approve','approved']],string='State', default="draft")
    attend_reason = fields.Text('Reasons')
    action_to_do = fields.Selection(
        selection=[('new_record', 'New Record'), ('modification', 'Modification')],
        string='Action To Do'
    )

    attendance_action = fields.Many2one(
        'hr.attendance',
        string='Attendance',
        # attrs={'invisible': [('action_to_do', '=', 'new_record')]}
    )
    check_in = fields.Datetime(string='Check-In')

    check_out = fields.Datetime(string='Check-Out')

    @api.onchange("emp_name")
    def _onchange_field(self):
        return {"domain":{'attendance_action':[("employee_id",'in',self.emp_name.ids)]}}
    
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft'    , 'waiting approve'),
                   ('waiting approve'    , 'draft'),  
                   ('waiting approve', 'approved' ),
                   ('approved', 'waiting approve' ),
                   ('approved', 'draft' ),
                   ]  
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
    
    def make_rejected(self):
        self.change_state('draft')
    
    @api.model
    def create(self, vals):
        if vals.get('sequence', _('New')) == _('New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code(
                'attendance.attendance') or _('New')
        res = super(Attendance, self).create(vals)
        return res