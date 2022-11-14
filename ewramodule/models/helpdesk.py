from odoo import models, fields,api ,_
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
import base64
from datetime import datetime, date, timedelta, time
class ModelName(models.Model):
    _inherit = 'helpdesk.ticket'
    
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
            'complainername':vals['complainer'],
            'national_id':vals['complainer_id'],
            'governate':vals['governate'],
            'city':vals['city'],
            'adress':vals['adress'],
            'complainer_tele':vals['tele'],
            'complaineremail':vals['email'],
            'responsableparty':vals['responsable'],
            'serviceprovider':vals['introducer'],
            'complaintype':vals['complain_class'],
            'complainreason':vals['complain_type'],
            'subscriptionnumber':vals['Subscription_id'],
            'areanumber':vals['origin_num'],
            'reportingway':vals['reportingway'],
            'reportingcode':vals['reporting_id'],
            'complaindate':vals['reportdate'],
            'complainresponsedate':vals['replay_date'],
            'providerresponse':vals['replay'],
            # '':vals[''],
            # '':vals[''],
            
        }
        # tmp_issue = self.env['helpdesk.ticket'].sudo().new(values)
        # values = tmp_issue._convert_to_write(tmp_issue._cache)
        myissue = self.env['helpdesk.ticket'].sudo().create(values)
        return {
            'id': myissue.id
        }
    

    
