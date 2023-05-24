# -*- coding: utf-8 -*-
# from odoo import http


# class CheckList(http.Controller):
#     @http.route('/check_list/check_list', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/check_list/check_list/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('check_list.listing', {
#             'root': '/check_list/check_list',
#             'objects': http.request.env['check_list.check_list'].search([]),
#         })

#     @http.route('/check_list/check_list/objects/<model("check_list.check_list"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('check_list.object', {
#             'object': obj
#         })
