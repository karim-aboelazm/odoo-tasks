# -*- coding: utf-8 -*-


from odoo import models, fields, api,_
from odoo.exceptions import UserError
class BatchPayment(models.Model):
    _name = 'batch.payment'
    _description = 'Batch installment Payment'

    sequence = fields.Char(string='Sequence', required=True,readonly=True, default=lambda self: _('New'))
    vendor = fields.Many2one('res.partner', string='Vendor')
    purchase_orders = fields.Many2many('purchase.order', string='P.O' , domain="[('partner_id', '=', vendor)]")
    contracts = fields.Many2many('fleet.vehicle.log.contract', string='Contracts', domain="[('purchase_order_id', '=', purchase_orders),('state','=','open')]")
    vehicle_lines = fields.One2many('vehicle.line','batch_payment', string="Vehicle Lines")
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    pay_ownership_value = fields.Boolean(string='Pay Ownership Value')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('generated', 'Draft'),
        ('paid', 'Paid'),
        ('closed', 'Closed'),
    ], string='State', default='draft')

    sum_monthly_amount = fields.Float("Amount",default=0.0)
        
    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('draft'    , 'confirmed'),  
                   ('confirmed', 'draft' ),
                   ('confirmed', 'paid' ),
                   ('draft'    , 'closed' ),
                   ('paid'    , 'closed' ),
                   ('confirmed', 'closed' ),
                   ('closed', 'confirmed' ),
                   ]  
        return (old_state, new_state) in allowed

    def change_state(self, new_state): 
        for bit in self:  
            if bit.is_allowed_transition(bit.state, new_state): 
                bit.state = new_state 
            else:
                continue

    def make_confirmed(self):
        self.change_state('confirmed')

    def make_closed(self):
        self.change_state('closed')
   
    @api.onchange('pay_ownership_value')
    def method_to_run(self):
        if self.pay_ownership_value:
            self.generate()
        
    def generate(self):
        for rec in self:
            rec.sum_monthly_amount = 0
            domain = [
                ('due_date', '>=', rec.date_from),
                ('due_date', '<=', rec.date_to),
                ('status', 'in', ['draft', 'partialy_paid']),
                ('fleet_contract', 'in', rec.contracts.ids),
                ('monthly_amount', '>', 0),
            ]
            domain_pay_ownership_value = [
                ('due_date', '=', False),
                ('status', 'in', ['draft', 'partialy_paid']),
                ('fleet_contract', 'in', rec.contracts.ids),
                ('monthly_amount', '>', 0),
            ]
            
            rec.vehicle_lines = rec.env['vehicle.line'].search(domain)
            
            if rec.pay_ownership_value:
                rec.vehicle_lines += rec.env['vehicle.line'].search(domain_pay_ownership_value)
            else:
                rec.vehicle_lines -= rec.env['vehicle.line'].search(domain_pay_ownership_value)
            rec.change_state('generated')
            
            for line in rec.vehicle_lines:
                rec.sum_monthly_amount += line.remaining_amount

    def pay(self):
        self.ensure_one()
        for rec in self:
            for line in rec.vehicle_lines:
                amount_for_pay = rec.sum_monthly_amount
                if amount_for_pay >= line.remaining_amount:
                    remain_after_pay = amount_for_pay - line.remaining_amount
                    line.write({
                        'remaining_amount': remain_after_pay,
                    })  
                    # raise UserError("Remain_After_Pay >= 0")
                else:
                    # line.write({
                    #     'paid_amount': line.remaining_amount,
                    #     'remaining_amount': remain_after_pay,
                    #     'status': 'partialy_paid',
                    # }) 
                    raise UserError("Remain_After_Pay < 0")
                
                rec.sum_monthly_amount = remain_after_pay
            rec.change_state('paid')
    
    def payment(self):
        pass

    @api.model
    def create(self, vals):
        if vals.get('sequence', _('New')) == _('New'):
            vals['sequence'] = self.env['ir.sequence'].next_by_code(
                'batch.payment') or _('New')
        res = super(BatchPayment, self).create(vals)
        return res