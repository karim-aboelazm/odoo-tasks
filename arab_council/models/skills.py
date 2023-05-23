# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Skills(models.Model):
    _name = 'arab_council.skills'
    skills = fields.Text(string="Skills")
    cv = fields.Binary('CV')