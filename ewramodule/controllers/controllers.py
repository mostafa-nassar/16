# -*- coding: utf-8 -*-
# from odoo import http


# class Ewramodule(http.Controller):
#     @http.route('/ewramodule/ewramodule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ewramodule/ewramodule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ewramodule.listing', {
#             'root': '/ewramodule/ewramodule',
#             'objects': http.request.env['ewramodule.ewramodule'].search([]),
#         })

#     @http.route('/ewramodule/ewramodule/objects/<model("ewramodule.ewramodule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ewramodule.object', {
#             'object': obj
#         })
