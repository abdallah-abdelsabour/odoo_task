# -*- coding: utf-8 -*-
# from odoo import http


# class PurSolution(http.Controller):
#     @http.route('/pur_solution/pur_solution', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pur_solution/pur_solution/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pur_solution.listing', {
#             'root': '/pur_solution/pur_solution',
#             'objects': http.request.env['pur_solution.pur_solution'].search([]),
#         })

#     @http.route('/pur_solution/pur_solution/objects/<model("pur_solution.pur_solution"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pur_solution.object', {
#             'object': obj
#         })
