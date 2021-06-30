# -*- coding: utf-8 -*-
# from odoo import http


# class DoctorModule(http.Controller):
#     @http.route('/doctor__module/doctor__module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/doctor__module/doctor__module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('doctor__module.listing', {
#             'root': '/doctor__module/doctor__module',
#             'objects': http.request.env['doctor__module.doctor__module'].search([]),
#         })

#     @http.route('/doctor__module/doctor__module/objects/<model("doctor__module.doctor__module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('doctor__module.object', {
#             'object': obj
#         })
