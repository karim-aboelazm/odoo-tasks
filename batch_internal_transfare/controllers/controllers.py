# -*- coding: utf-8 -*-
# from odoo import http


# class BatchInternalTransfare(http.Controller):
#     @http.route('/batch_internal_transfare/batch_internal_transfare', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/batch_internal_transfare/batch_internal_transfare/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('batch_internal_transfare.listing', {
#             'root': '/batch_internal_transfare/batch_internal_transfare',
#             'objects': http.request.env['batch_internal_transfare.batch_internal_transfare'].search([]),
#         })

#     @http.route('/batch_internal_transfare/batch_internal_transfare/objects/<model("batch_internal_transfare.batch_internal_transfare"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('batch_internal_transfare.object', {
#             'object': obj
#         })
