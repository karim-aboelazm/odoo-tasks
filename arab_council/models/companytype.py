# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CompanyType(models.Model):
    _name   = "arab_council.company_type"
    name    = fields.Char(string="Company Type", max_length=100)