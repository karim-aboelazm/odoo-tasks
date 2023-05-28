# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class PropertyReservation(models.Model):
    _name = "new_fields.property.reservation"
    _rec_name = "referance"
    referance = fields.Char(string='Referance', required=True,readonly=True, default=lambda self: 'New')
    status = fields.Selection([(i, i.title()) for i in ["draft","confirmed",'canceled']], string="Status", default='draft')
    sales_person   = fields.Char(srting="Sales Person")
    customer   = fields.Many2many('res.partner',srting="Customer")
    date_of_res = fields.Date("Date Of Reservation")
    payment_date= fields.Date("Payment Date")
    analytic_account = fields.Char("Analytic Account")
    income_account = fields.Char("Income Account")
    property_price = fields.Float("Property Price")
    res_amount = fields.Float("Reservation Amount")
    taxes = fields.Text("Taxes")
    entry = fields.Text("Entry")
    property_no = fields.Integer("Property")
    property_code = fields.Char("Code")
    property_floor = fields.Integer("Floor") 
    address = fields.Char("Address")
    property_type = fields.Char("Property Type")
    property_status = fields.Char("Property Status")
    property_area = fields.Integer("Property Area")
    frtecn       = fields.Char("First residence tax exemption certificate number", compute="_compute_field")
    reservation_end_date = fields.Date("Reservation End Date",required=True)
    
    @api.depends('customer')
    def _compute_field(self):
        for record in self:
            record.frtecn = record.customer.frtecn
    
    def confirm_reservation(self):
        self.status = 'confirmed'

    def cancel_reservation(self):
        self.status = 'canceled'
        
    def check_reservation_end_date(self):
        today = date.today()
        for record in self:
            record.reservation_end_date = today
            record.status = 'canceled'
    @api.model
    def create(self, vals):
        if vals.get('referance', 'New') == 'New':
            vals['referance'] = self.env['ir.sequence'].next_by_code('new_fields.property.reservation') or 'New'
        res = super(PropertyReservation, self).create(vals)
        return res
   