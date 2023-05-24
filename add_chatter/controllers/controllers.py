# -*- coding: utf-8 -*-
# from odoo import http


# class AddChatter(http.Controller):
#     @http.route('/add_chatter/add_chatter', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/add_chatter/add_chatter/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('add_chatter.listing', {
#             'root': '/add_chatter/add_chatter',
#             'objects': http.request.env['add_chatter.add_chatter'].search([]),
#         })

#     @http.route('/add_chatter/add_chatter/objects/<model("add_chatter.add_chatter"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('add_chatter.object', {
#             'object': obj
#         })
