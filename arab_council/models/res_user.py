from odoo import models, fields, api

class Users(models.Model):
    _inherit  = "res.users"
    is_portal = fields.Boolean(compute='_is_portal')
    types = fields.Selection([('company', 'Company'),('expert', 'Expert')], string='Portal Types')
    companies = fields.Many2many('arab_council.company',relation='user_newcompany')
    experts = fields.Many2many('arab_council.expert')

    def show_portal(self):
        action = {
            'type': 'ir.actions.act_window',
            'name': 'Portal',
            'view_mode': 'tree,form',
            'target': 'current',
        }
        if self.types == 'company':
            action['res_model'] = 'company'
            action['domain'] = "[('id', 'in', self.companies.ids)]"
        elif self.types == 'expert':
            action['res_model'] = 'expert'
            action['domain'] = "[('id', 'in', self.experts.ids)]"

        return action


    def _is_portal(self):
        self.ensure_one()
        self.is_portal = self.has_group('base.group_portal')

    