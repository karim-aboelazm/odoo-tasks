# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WorkField(models.Model):
    _name           = "arab_council.work_field"
    name = fields.Char(string="Work Field Name")
