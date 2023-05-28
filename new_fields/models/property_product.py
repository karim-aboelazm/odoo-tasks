# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
class PropertyProduct(models.Model):
    _name = "new_fields.property.product"
    property_name = fields.Char("Property Name")
    property_code = fields.Char("Property Code")
    property_image= fields.Image()
    
    
    property_type = fields.Char("Property Type")
    property_price = fields.Float("Property Price")
    sales_person   = fields.Many2many('res.partner',srting="Sales Person")
    property_age = fields.Integer("Property Age")
    constraction_status = fields.Char("Constraction Status")
    
    building = fields.Char("Building")
    project = fields.Char("Project")
    cost = fields.Float("Cost")
    
    type_of_property = fields.Char("Type Of Property")
    property_floor = fields.Integer("Property Floor")
    
    property_area = fields.Integer("Property Area")
    net_property_area = fields.Integer("Net Property Area ")
    rooms = fields.Integer("Rooms")
    bath_rooms = fields.Integer("Bathrooms")
    property_form=fields.Char("Property Form")
    property_number=fields.Char("Property number")
    land_area = fields.Float("Land area")
    building_flats = fields.Float("Building flats")
    ground_floor_area = fields.Float("Ground floor area")
    first_floor_space = fields.Float("First floor space")
    second_floor_space = fields.Float("Second floor space")
    basement_space = fields.Float("basement space")
    piece_number= fields.Char("piece number")
    approved_scheme_number= fields.Char("Approved scheme number")
    waranty = fields.Binary(string='PDF File', attachment=True, filename="*.pdf" , mimetypes='application/pdf')
    @api.constrains('waranty')
    def _check_pdf_file(self):
        for record in self:
            if record.waranty:
                if not record.waranty.decode().endswith('.pdf'):
                    raise ValidationError('Please upload a PDF file.')