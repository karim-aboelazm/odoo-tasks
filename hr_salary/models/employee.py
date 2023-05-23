# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrSalary(models.Model):
    _inherit             = 'hr.employee'
    name                 = fields.Char()
    employee_id          = fields.Char("Employee ID")
    employee_arabic_name = fields.Char()
      
