# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company(models.Model):
    _name           = "arab_council.company"
    
    name            = fields.Char(string="Company Name",max_length=100)
    compnay_type    = fields.Many2one(string="Company Type",comodel_name="arab_council.company_type")
    launching_date  = fields.Date(string="Launching Date")
    goals           = fields.Char(string="Company Goals", max_length=100)
    contact         = fields.Many2one(string="Contact",comodel_name="res.partner")
    email           = fields.Char(string="Email" , widget='email')
    website         = fields.Char(string="Website")
    country_id      = fields.Many2one('res.country', string='Country')
    state_id        = fields.Many2one('res.country.state', string='State')
    city            = fields.Char(string='City')
    zip_code        = fields.Char(string='Zip Code')
    street          = fields.Char(string='Street')
    review_rating   = fields.Selection([(f'{i}', f'{i} Star') for i in range(6)],string='Rating')
    work_field      = fields.Many2many(string="Work Field",comodel_name="arab_council.work_field")
    work_history    = fields.One2many(string="Work History",comodel_name="arab_council.work_history",inverse_name="company_hist")

    
    