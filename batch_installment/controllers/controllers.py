# -*- coding: utf-8 -*-
# from odoo import http


# class BatchInstallment(http.Controller):
#     @http.route('/batch_installment/batch_installment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/batch_installment/batch_installment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('batch_installment.listing', {
#             'root': '/batch_installment/batch_installment',
#             'objects': http.request.env['batch_installment.batch_installment'].search([]),
#         })

#     @http.route('/batch_installment/batch_installment/objects/<model("batch_installment.batch_installment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('batch_installment.object', {
#             'object': obj
#         })
