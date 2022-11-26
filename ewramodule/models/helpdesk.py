
from odoo import models, fields,api ,_
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
import base64
from datetime import datetime, date, timedelta, time
import secrets
class ModelName(models.Model):
    _inherit = 'helpdesk.ticket'
    #_sql_constraints = [('unique_code', 'unique(complaincode)', 'La référence doit être unique !')]
    complaincode = fields.Char(string='رقم الشكوي', store=True,compute='_compute_complaincode' )
    
    @api.depends('name')
    def _compute_complaincode(self):        
        for record in self:
            if record.id:
                record.complaincode = str(secrets.token_hex(1))+str(record.id)
    
    
   
    
    governate=fields.Many2one(comodel_name='ewra_governate',string='المحافظة')
    complaintype=fields.Many2one(comodel_name='ticket.classfication',string='نوع الشكوى')
    complainreason=fields.Many2one(comodel_name='ticket.type',string='سبب الشكوي')
    responsableparty=fields.Many2one(comodel_name='res.partner',string='الجهة المسئولة')
    serviceprovider=fields.Many2one(comodel_name='res.partner',string='مقدم الخدمة')
    reportingway=fields.Many2one(comodel_name='reportingway',string='وسيلة الإبلاغ')
    #complain_source=fields.Many2one(comodel_name="",string='مصدر الشكوى')
    complainername=fields.Char(string="إسم الشاكى")
    complaineremail=fields.Char(string="البريد الإلكتروني")
    national_id=fields.Char("رقم البطاقه")
    city=fields.Char(string='قسم/ قرية/ مركز')
    adress=fields.Char(string='عنوان الشاكى')
   
    subscriptionnumber=fields.Char(string='رقم الاشتراك')
    areanumber=fields.Char(string="رقم المنطقة")
    complainer_tele=fields.Char(string="تليفون العميل")
    reportingcode=fields.Char(string='كود الشكوى')
    complaindate=fields.Date(string='تاريخ الإبلاغ')
    
    
    
    complainresponsedate=fields.Char(string='تاريخ رد الشركة')
    providerresponse=fields.Text(string='رد مقدم الخدمة',
    track_visibility='onchange'
    )
    @api.model
    def create_help_ticket_portal(self,vals):
        # if not (self.env.user.employee_id):
        #     raise AccessDenied()
        #user = self.env.user
        #self = self.sudo()
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
        tmp_issue = self.env['helpdesk.ticket'].sudo().new(values)
        values = tmp_issue._convert_to_write(tmp_issue._cache)
        myissue = self.env['helpdesk.ticket'].sudo().create(values)
        #raise UserWarning(str(myissue.id))
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
    

    
