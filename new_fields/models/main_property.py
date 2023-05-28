# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
class MainProperty(models.Model):
   _name = "new_fields.main.property"
   name = fields.Char("Name")
   code = fields.Char("Code")
   project = fields.Char("Project")
   total_cost = fields.Char("Total Cost")
   date = fields.Date("Date")
   launch_date = fields.Date("Launching Date")
   
   property_status = fields.Char("Property Status")
   property_type = fields.Char("Type Of Property")
   property_price = fields.Float("Property Price")
   lan_area = fields.Integer("Lan Area")
   lan_area = fields.Integer("Lan Area ㎡ ")
   constraction_date = fields.Date("Constraction Date")
   price = fields.Float("Property Price")
   floors = fields.Integer("#Floors")
   unit_per_floors = fields.Integer("#Unit Per Floors")
   
   waranty = fields.Binary(string='PDF File', attachment=True, filename="*.pdf" , mimetypes='application/pdf')
   @api.constrains('waranty')
   def _check_pdf_file(self):
      for record in self:
         if record.waranty:
            if not record.waranty.decode().endswith('.pdf'):
               raise ValidationError('Please upload a PDF file.')