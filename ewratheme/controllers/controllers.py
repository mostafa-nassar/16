# # -*- coding: utf-8 -*-
# # from odoo import http
# from odoo import http
# from odoo.http import request

# class WebsiteHelpdesk_portal(http.Controller):

#     @http.route('''/ewra-helpdesk-data''', type='json', auth="user", website=True,
#                 sitemap=True)
#     def website_helpdesk_view(self, **kwargs):
#         #partners = request.env['res.partner'].search([('is_complaint','=',True)])
#         #issues = request.env['complain.issue'].search([])
#         #drinking_watters = request.env['drinking.water'].search([])
#         clasifications=request.env['ticket.classfication'].search([])
#         classfication=clasifications.mapped(lambda record: {'id':record.id ,'name': record.name})
#         governments=request.env['ewra_governate'].search([])
#         governs=governments.mapped(lambda record: {'id':record.id ,'name': record.name})
#         reportingways=request.env['reportingway'].search([])
#         reportingway=reportingways.mapped(lambda record: {'id':record.id ,'name': record.name})
#         responsaplepartys=request.env['res.partner'].search([('companytype','=','complainers')])
#         responsapleparty=responsaplepartys.mapped(lambda record: {'id':record.id ,'name': record.name})
#         return { 'classfications':classfication,'governments':governs,'reportingway':reportingway,'responsapleparty':responsapleparty}
        
#         return request.render("ewratheme.ewra_complaint_form"
#                               , {
#                                 'classfications':clasifications,
#                                 #'partners': partners,
#                                 #'issues': issues,
#                                 #'types': drinking_watters,
#                               }
#                               )
#     @http.route('''/ewra-complain_changereason''', type='json', auth="user", website=True,
#                 sitemap=True)
#     def website_helpdesk_change_reason(self, **kwargs):
#         #partners = request.env['res.partner'].search([('is_complaint','=',True)])
#         #issues = request.env['complain.issue'].search([])
#         #drinking_watters = request.env['drinking.water'].search([])
        
#         clasifications=request.env['ticket.type'].search([('TicketClassfication','=',int(kwargs['id']))])
        
#         classfication=clasifications.mapped(lambda record: {'id':record.id ,'name': record.name})
#         return { 'types':classfication,}
#         return request.render("ewratheme.ewra_complaint_form"
#                               , {
#                                 'classfications':clasifications,
#                                 #'partners': partners,
#                                 #'issues': issues,
#                                 #'types': drinking_watters,
#                               }
#                               )
#     @http.route('''/ewra-complain_introducer''', type='json', auth="user", website=True,
#                 sitemap=True)
#     def website_helpdesk_change_introducer(self, **kwargs):
#         #partners = request.env['res.partner'].search([('is_complaint','=',True)])
#         #issues = request.env['complain.issue'].search([])
#         #drinking_watters = request.env['drinking.water'].search([])
        
#         introducers=request.env['res.partner'].search([('complainers','=',int(kwargs['id']))])
        
#         introducer=introducers.mapped(lambda record: {'id':record.id ,'name': record.name})
#         return { 'types':introducer,}    