# -*- coding: utf-8 -*-
# from odoo import http


# class NewFields(http.Controller):
#     @http.route('/new_fields/new_fields', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_fields/new_fields/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_fields.listing', {
#             'root': '/new_fields/new_fields',
#             'objects': http.request.env['new_fields.new_fields'].search([]),
#         })

#     @http.route('/new_fields/new_fields/objects/<model("new_fields.new_fields"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_fields.object', {
#             'object': obj
#         })
