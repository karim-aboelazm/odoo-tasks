# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FleetContract(models.Model):
    _inherit = 'fleet.vehicle.log.contract'
    
    state = fields.Selection(
        [('futur', 'New'),
         ('open', 'In Progress'),
         ('paid', 'Paid'),
         ('closed', 'Closed')
        ], 'Status', default='open', readonly=True,
        help='Choose whether the contract is still valid or not',
        tracking=True,
        copy=False) 
    purchase_order_id = fields.Many2one('purchase.order',string="Reference")
    pay_ownership_value = fields.Float(string='Pay Ownership Value')
    vehicle_lines = fields.One2many('vehicle.line','fleet_contract')
    