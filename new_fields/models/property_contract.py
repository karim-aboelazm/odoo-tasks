# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class ContractProperty(models.Model):
    _name = "new_fields.contract.property"
    
    referance = fields.Char(string='Referance', required=True,readonly=True, default=lambda self: 'New')
    status = fields.Selection([(i, i.title()) for i in ["draft","confirmed",'canceled']], string="Status", default='draft')
    sales_person   = fields.Char(srting="Sales Person")
    customer   = fields.Many2many('res.partner',srting="Customer")
    date_of_contract = fields.Date("Date Of Contract")
    first_payment = fields.Float("First Payment")
    analytic_account = fields.Char("Analytic Account")
    income_account = fields.Char("Income Account")
    reservation =fields.Char('Reservation')
    partial_payment = fields.Float("Partial Payment")
    note = fields.Text("Note")
    taxes = fields.Boolean("Taxes")
    
    # payment_date= fields.Date("Payment Date")
    property_no = fields.Integer("Property")
    property_code = fields.Char("Code")
    property_floor = fields.Integer("Floor") 
    address = fields.Char("Address")
    property_type = fields.Char("Property Type")
    property_status = fields.Char("Property Status")
    property_area = fields.Integer("Property Area")
    property_price = fields.Float("Property Price")
    entry = fields.Text("Enter")
    contract_number = fields.Char("Contract Number")
    contracting_place = fields.Char("Contracting Place")
    real_state_tax = fields.Char("Real State Tax")
   
    def confirm_contract(self):
        self.status = 'confirmed'

    def cancel_contract(self):
        self.status = 'canceled'
        
    
    @api.model
    def create(self, vals):
        if vals.get('referance', 'New') == 'New':
            vals['referance'] = self.env['ir.sequence'].next_by_code('new_fields.property.contract') or 'New'
        res = super(ContractProperty, self).create(vals)
        return res
   