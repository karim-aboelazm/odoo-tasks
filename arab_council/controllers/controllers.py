# -*- coding: utf-8 -*-
# from odoo import http


# class ArabCouncil(http.Controller):
#     @http.route('/arab_council/arab_council', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arab_council/arab_council/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('arab_council.listing', {
#             'root': '/arab_council/arab_council',
#             'objects': http.request.env['arab_council.arab_council'].search([]),
#         })

#     @http.route('/arab_council/arab_council/objects/<model("arab_council.arab_council"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arab_council.object', {
#             'object': obj
#         })
