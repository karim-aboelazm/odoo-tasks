# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EmployeeCheckList(models.Model):
    _name = 'check_list.employee.check.list'
    _rec_name = 'document_name'
    document_name = fields.Char(string="Document Name")
    checklist_type = fields.Char(string="Checklist Type")