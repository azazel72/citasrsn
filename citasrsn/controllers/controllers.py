# -*- coding: utf-8 -*-
from odoo import http
class Citasrsn(http.Controller):
     @http.route('/citasrsn/citasrsn/', auth='public')
     def index(self, **kw):
         return "Hello, world"

#     @http.route('/citasrsn/citasrsn/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('citasrsn.listing', {
#             'root': '/citasrsn/citasrsn',
#             'objects': http.request.env['citasrsn.citasrsn'].search([]),
#         })

#     @http.route('/citasrsn/citasrsn/objects/<model("citasrsn.citasrsn"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('citasrsn.object', {
#             'object': obj
#         })
