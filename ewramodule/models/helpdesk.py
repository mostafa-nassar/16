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
    providerresponse=fields.Text(string='رد مقدم الخدمة')
    @api.model
    def create_help_ticket_portal(self,vals):
        # if not (self.env.user.employee_id):
        #     raise AccessDenied()
        # user = self.env.user
        # self = self.sudo()
        values={
            'name': 'شكوي'+' '+ (vals['complainer'] if 'complainer' in vals else ''),
            'complainername':vals['complainer'] if 'complainer' in vals else False,
            'national_id':vals['complainer_id'] if 'complainer_id' in vals else False,
            'governate':vals['governate'] if 'governate' in vals else False,
            'city':vals['city'] if 'city' in vals else False,
            'adress':vals['adress'] if 'adress' in vals else False,
            'complainer_tele':vals['tele'] if 'tele' in vals else False,
            'complaineremail':vals['email'] if 'email' in vals else False,
            'responsableparty':vals['responsable'] if 'responsable' in vals else False,
            'serviceprovider':vals['introducer'] if 'introducer' in vals else False,
            'complaintype':vals['complain_class'] if 'complain_class' in vals else False,
            'complainreason':vals['complain_type'] if 'complain_type' in vals else False,
            'subscriptionnumber':vals['Subscription_id'] if 'Subscription_id' in vals else False,
            'areanumber':vals['origin_num'] if 'origin_num' in vals else False,
            'reportingway':vals['reportingway'] if 'reportingway' in vals else False,
            'reportingcode':vals['reporting_id'] if 'reporting_id' in vals else False,
            'complaindate':vals['reportdate'] if 'reportdate' in vals else False,
            'complainresponsedate':vals['replay_date'] if 'replay_date' in vals else False,
            'providerresponse':vals['replay'] if 'replay' in vals else False,
            # '':vals[''],
            # '':vals[''],
            
        }
        # tmp_issue = self.env['helpdesk.ticket'].sudo().new(values)
        # values = tmp_issue._convert_to_write(tmp_issue._cache)
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
    

    
