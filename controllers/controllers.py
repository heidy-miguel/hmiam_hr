# -*- coding: utf-8 -*-
# from odoo import http


# class HmiamHr(http.Controller):
#     @http.route('/hmiam_hr/hmiam_hr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hmiam_hr/hmiam_hr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hmiam_hr.listing', {
#             'root': '/hmiam_hr/hmiam_hr',
#             'objects': http.request.env['hmiam_hr.hmiam_hr'].search([]),
#         })

#     @http.route('/hmiam_hr/hmiam_hr/objects/<model("hmiam_hr.hmiam_hr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hmiam_hr.object', {
#             'object': obj
#         })
