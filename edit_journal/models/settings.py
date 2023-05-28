from odoo import models, fields
from datetime import timedelta

class ResUsers(models.TransientModel):
    _inherit = 'res.config.settings'
    number_before_sending = fields.Integer(string="Number Before Sending")
    notification_users  = fields.Many2many('res.partner', string='Notification Users')

    def generate_new_activities(self):
        activity_model = self.env['mail.activity']
        payment_model = self.env['account.payment']
        for partner in self.notification_users:
            payments = payment_model.search([('partner_id', '=', partner.id)])
            for payment in payments:
                due_date = payment.new_date  
                if due_date:
                    notification_date = due_date - timedelta(days=self.number_before_sending)
                    activity = activity_model.create({
                        'res_id': payment.id,
                        'res_model_id': self.env['ir.model']._get_id('account.payment'),
                        'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                        'summary': 'Notification',
                        'date_deadline': notification_date,
                        'note': 'This is a notification for payment %s' % payment.name,
                        'user_id': False # this enable to send activity for user or partners..
                    })
                    partner.message_post_with_view(
                        'mail.message_activity_done',
                        subtype_id=self.env.ref('mail.mt_activities').id,
                        context={'default_activity_ids': [activity.id]}
                    )
