# -*- coding: utf-8 -*-
# from odoo import http


# class EditJournal(http.Controller):
#     @http.route('/edit_journal/edit_journal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edit_journal/edit_journal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('edit_journal.listing', {
#             'root': '/edit_journal/edit_journal',
#             'objects': http.request.env['edit_journal.edit_journal'].search([]),
#         })

#     @http.route('/edit_journal/edit_journal/objects/<model("edit_journal.edit_journal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edit_journal.object', {
#             'object': obj
#         })
