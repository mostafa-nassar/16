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
from odoo import http
from odoo.http import request

class WebsiteHelpdesk_portal(http.Controller):
    #@http.route('''/ewra-helpdesk-data''', type='json', auth="user", website=True,
      #          sitemap=True)
    @http.route('''/ewra-helpdesk-data''', type='json', auth="public", website=True,
                sitemap=True)
    def website_helpdesk_view(self, **kwargs):
        #partners = request.env['res.partner'].search([('is_complaint','=',True)])
        #issues = request.env['complain.issue'].search([])
        #drinking_watters = request.env['drinking.water'].search([])
        clasifications=request.env['ticket.classfication'].search([])
        classfication=clasifications.mapped(lambda record: {'id':record.id ,'name': record.name})
        governments=request.env['ewra_governate'].search([])
        governs=governments.mapped(lambda record: {'id':record.id ,'name': record.name})
        reportingways=request.env['reportingway'].search([])
        reportingway=reportingways.mapped(lambda record: {'id':record.id ,'name': record.name})
        responsaplepartys=request.env['res.partner'].sudo().search([('companytype','=','responsable')])
        responsapleparty=responsaplepartys.mapped(lambda record: {'id':record.id ,'name': record.name})
        return { 'classfications':classfication,'governments':governs,'reportingway':reportingway,'responsapleparty':responsapleparty}
        
        return request.render("ewramodule.ewra_complaint_form"
                              , {
                                'classfications':clasifications,
                                #'partners': partners,
                                #'issues': issues,
                                #'types': drinking_watters,
                              }
                              )
    # @http.route('''/ewra-complain_changereason''', type='json', auth="user", website=True,
    #             sitemap=True)
    @http.route('''/ewra-complain_changereason''', type='json', auth="public", website=True,
                sitemap=True)
    def website_helpdesk_change_reason(self, **kwargs):
        #partners = request.env['res.partner'].search([('is_complaint','=',True)])
        #issues = request.env['complain.issue'].search([])
        #drinking_watters = request.env['drinking.water'].search([])
        
        clasifications=request.env['ticket.type'].search([('TicketClassfication','=',int(kwargs['id']))])
        
        classfication=clasifications.mapped(lambda record: {'id':record.id ,'name': record.name})
        return { 'types':classfication,}
        return request.render("ewratheme.ewra_complaint_form"
                              , {
                                'classfications':clasifications,
                                #'partners': partners,
                                #'issues': issues,
                                #'types': drinking_watters,
                              }
                              )
    @http.route('''/ewra-complain_introducer''', type='json', auth="public", website=True,
                sitemap=True)
    def website_helpdesk_change_introducer(self, **kwargs):
        #partners = request.env['res.partner'].search([('is_complaint','=',True)])
        #issues = request.env['complain.issue'].search([])
        #drinking_watters = request.env['drinking.water'].search([])
        
        introducers=request.env['res.partner'].sudo().search([('responsables','=',int(kwargs['id']))])
        
        introducer=introducers.mapped(lambda record: {'id':record.id ,'name': record.name})
        return { 'types':introducer,} 
    @http.route('''/ewra-complain_submit''', type='json', auth="public", website=True,
                sitemap=True)
    def website_helpdesk_submited(self, **vals):
      values={
            'name': 'شكوي'+' '+ (vals['complainername'] if 'complainername' in vals else ''),
            'complainername':vals['complainername'] if 'complainername' in vals else False,
            'national_id':vals['national_id'] if 'national_id' in vals else False,
            'governate':vals['governate'] if 'governate' in vals else False,
            'city':vals['city'] if 'city' in vals else False,
            'adress':vals['adress'] if 'adress' in vals else False,
            'complainer_tele':vals['complainer_tele'] if 'complainer_tele' in vals else False,
            'complaineremail':vals['complaineremail'] if 'complaineremail' in vals else False,
            'responsableparty':vals['responsableparty'] if 'responsableparty' in vals else False,
            'serviceprovider':vals['serviceprovider'] if 'serviceprovider' in vals else False,
            'complaintype':vals['complaintype'] if 'complaintype' in vals else False,
            'complainreason':vals['complainreason'] if 'complainreason' in vals else False,
            'subscriptionnumber':vals['subscriptionnumber'] if 'subscriptionnumber' in vals else False,
            'areanumber':vals['areanumber'] if 'areanumber' in vals else False,
            'reportingway':vals['reportingway'] if 'reportingway' in vals else False,
            'reportingcode':vals['reportingcode'] if 'reportingcode' in vals else False,
            'complaindate':vals['complaindate'] if 'complaindate' in vals else False,
            'complainresponsedate':vals['complainresponsedate'] if 'complainresponsedate' in vals else False,
            'providerresponse':vals['providerresponse'] if 'providerresponse' in vals else False,
            'description':vals['description'] if 'description' in vals else False,
            # '':vals[''],
            # '':vals[''],
            
        }
      request.env['helpdesk.ticket'].sudo().create(values)#create_help_ticket_portal(kwargs)
      return {
            'code': """
            
            <div id="wrap">
                    <div class="oe_structure oe_empty">
                        <div class="container text-success oe_subdescription center center-content align-center text-center">
                            <br/><br/>
                            <div class="row justify-content-center">
                           
                                <div class="col-md-4">
                                    <div class="alert alert-success">
                                        تم ارسال الشكوي بنجاح
                                        <i class="fa fa-thumbs-o-up fa-2x">
                                        </i>

                                        <p>
                                            <h5>رقم الشكوي
                                               """+myissue.complaincode+"""
                                            </h5>
                                        </p>
                                    </div>
                                  
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </div>
              
            """
            }