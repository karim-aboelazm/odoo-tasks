# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EditResPartner(models.Model):
    _inherit     = 'res.partner'
    nationality  = fields.Many2one('res.country',string='Nationality')
    id_number    = fields.Char("Identification Number")
    frtecn       = fields.Char("First residence tax exemption certificate number")
    fcob         = fields.Char("Finance company or bank")
    fcn          = fields.Char("Financing contract number")
    dob          = fields.Date("Date of Birth")

    
