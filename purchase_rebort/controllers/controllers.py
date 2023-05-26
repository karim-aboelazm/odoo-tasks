# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseRebort(http.Controller):
#     @http.route('/purchase_rebort/purchase_rebort', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_rebort/purchase_rebort/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_rebort.listing', {
#             'root': '/purchase_rebort/purchase_rebort',
#             'objects': http.request.env['purchase_rebort.purchase_rebort'].search([]),
#         })

#     @http.route('/purchase_rebort/purchase_rebort/objects/<model("purchase_rebort.purchase_rebort"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_rebort.object', {
#             'object': obj
#         })
