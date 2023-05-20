# -*- coding: utf-8 -*-

from odoo import models, fields, api

class VehicleLine(models.Model):
    _name = 'vehicle.line'
    _description = 'Vehicle Line'
    line_number = fields.Integer("No.")
    due_date = fields.Date("Due Date")
    asset = fields.Float("Asset")
    interest = fields.Float("Interest")
    insurance = fields.Float("Insurance")
    monthly_amount = fields.Float("Monthly Amount")
    paid_amount = fields.Float("Paid Amount")
    remaining_amount = fields.Float("ٌRemaining Amount", compute='remainig_compute_field')
    fleet_contract = fields.Many2one('fleet.vehicle.log.contract')
    batch_payment = fields.Many2one('batch.payment')
    status = fields.Selection(
        [('draft', 'Draft'),
         ('posted', 'Posted'),
         ('partialy_paid', 'Partially Paid')
        ], 'Status', default='draft', readonly=True)

    @api.depends('paid_amount','monthly_amount')
    def remainig_compute_field(self):
        for req in self:
            req.remaining_amount = req.monthly_amount - req.paid_amount
            if req.monthly_amount > req.remaining_amount and req.remaining_amount > 0:
                req.status = 'partialy_paid'
            elif req.monthly_amount > req.remaining_amount and req.remaining_amount == 0:
                req.status = 'posted'
            elif req.monthly_amount == req.remaining_amount:
                req.status = 'draft'
            else:
                pass 
        
            
    
    
    
    
    
    