# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WorkHistory(models.Model):
    _name        = "arab_council.work_history"
    work_field   = fields.Many2one(string="Work Field",comodel_name="arab_council.work_field")
    year = fields.Selection([(str(year), str(year)) for year in range(1990, 2051)],string='Year')
    company_hist = fields.Many2one(string="Company History",comodel_name="arab_council.company")
    