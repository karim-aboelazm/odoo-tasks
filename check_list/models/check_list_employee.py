# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CheckListEmployees(models.Model):
    _inherit = 'hr.employee'
    check_list = fields.Many2many("check_list.employee.check.list")
    entry_progress = fields.Integer(string='Entry Progress' ,compute='_check_list_percentage')
    
    @api.depends('check_list')
    def _check_list_percentage(self):
        count_all_check_list = self.env['check_list.employee.check.list'].search_count([])
        for record in self:
            if count_all_check_list > 0 :
                record.entry_progress = (len(record.check_list)/count_all_check_list)*100
            else:
                record.entry_progress = 0
    
    
    