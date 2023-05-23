# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Expert(models.Model):
    _name           = 'arab_council.expert'
    _description    = 'Arab Council Experts'
    # general information 
    name            = fields.Char(string="Name",max_length=100)
    gender          = fields.Selection(string="Gender",selection=[('male', 'Male'),('female', 'Female')])
    birthday        = fields.Date(string="Birthday")
    job_position    = fields.Many2one(comodel_name='hr.job', string='Job Position')
    work_location   = fields.Char(string="Work location" , max_length=250)
    email           = fields.Char(string="Email" , widget='email')
    website         = fields.Char(string="Website")
    # Address collections 
    country_id      = fields.Many2one('res.country', string='Country')
    state_id        = fields.Many2one('res.country.state', string='State')
    city            = fields.Char(string='City')
    zip_code        = fields.Char(string='Zip Code')
    street          = fields.Char(string='Street')
    review_rating   = fields.Selection(
        [('0', '0 Star'),('1', '1 Star'), ('2', '2 Stars'), ('3', '3 Stars'), ('4', '4 Stars'), ('5', '5 Stars')],
        string='Rating'
    )
    # skills page 
    skills          = fields.Many2many('arab_council.skills',string="Skills")
    # additional information page
    work_phone      = fields.Char(string="Work Phone",max_length=15)    
    mobile          = fields.Char(string="Mobile",max_length=15) 
    home_phone      = fields.Char(string="Home Phone",max_length=15)    
    fax             = fields.Char(string="Fax",max_length=15)    
    # Bio page
    bio             = fields.Html(string='Bio')
    
     