# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployeeDocument(models.Model):
    _name           = 'add_chatter.hr.employee.document'
    _inherit        = ['mail.thread', 'mail.activity.mixin']
    document        = fields.Char("Document")
    document_number = fields.Integer("Document Number")
    issue_date      = fields.Date("Issue Date")
    expire_date     = fields.Date("Expire Date")
    attachment      = fields.Binary("Attachment")
    related_users   = fields.Many2one(comodel_name='res.users',string="User") 
    
    def send_user_message(self):
        self.ensure_one()
        partner_ids = self.env['res.users'].search([('id', '!=', self.env.user.id)]).mapped('partner_id')
        self.message_post(
            body="Hello, Users!",
            message_type='notification',
            subtype_xmlid='mail.mt_comment',
            partner_ids=[(4, partner_id.id) for partner_id in partner_ids],
        )
       
    def send_activity_log(self):
        self.activity_schedule(
        note="Activity log message",
        user_id=self.env.user.id,
    )
    
