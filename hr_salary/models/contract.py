# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contract(models.Model):
    _inherit            = 'hr.contract'
    allowance           = fields.One2many(string="Allowance", comodel_name="hr_salary.allowance", inverse_name="allow_id")
    deduction           = fields.One2many(string="Deduction", comodel_name="hr_salary.deduction", inverse_name="deduct_id")
    total_net_salary    = fields.Float(string="Total Salary",compute="_compute_total_net_salary")
    total_gross_salary  = fields.Float(string="Gross Salary",compute="_compute_total_gross_salary")

    @api.depends('allowance','wage')
    def _compute_total_gross_salary(self):
        for record in self:
            record.total_gross_salary = sum(record.allowance.mapped('amount')) + record.wage
    
    @api.depends('allowance','wage','deduction')
    def _compute_total_net_salary(self):
        for record in self:
            record.total_net_salary = sum(record.allowance.mapped('amount')) + record.wage - sum(record.deduction.mapped('amount')) 
    
    