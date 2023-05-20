# -*- coding: utf-8 -*-


from odoo import models, fields, api


class ResPart(models.Model):
    _inherit = 'res.partner'
    
    new_field = fields.Boolean()

    
