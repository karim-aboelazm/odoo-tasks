# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Allowance(models.Model):
    _name       = "hr_salary.allowance"
    amount      = fields.Float(string="Amount")
    allow_id    = fields.Many2one(string="Allowance",comodel_name="hr.contract")
    