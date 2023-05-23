# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Deduction(models.Model):
    _name       = "hr_salary.deduction"
    amount      = fields.Float(string="Amount")
    deduct_id   = fields.Many2one(string="Deduction",comodel_name="hr.contract")
    