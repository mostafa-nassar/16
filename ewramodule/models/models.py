# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class ewratheme(models.Model):
#     _name = 'ewratheme.ewratheme'
#     _description = 'ewratheme.ewratheme'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class ticketClassfication(models.Model):
    _name = "ticket.classfication"
    _description = 'tasnefshakwa'

    # _rec_name = 'name'
    # _order = 'name ASC'

    name = fields.Char(string='تصنيف الشكوي', required=True,copy=False)
    type=fields.One2many(comodel_name="ticket.type",inverse_name="TicketClassfication",string="نوع الشكوي")
    reason=fields.One2many(comodel_name="ticket.reason",inverse_name="TicketClassfication",string="سبب الشكوي")
class NoaShakwa(models.Model):
    _name = 'ticket.type'
    _description = 'NoaShakwa'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(string='نوع الشكوي',required=True,copy=False)
    TicketClassfication=fields.Many2one(comodel_name="ticket.classfication",string="تصنيف الشكوي")


class sababShakwa(models.Model):
    _name = 'ticket.reason'
    _description = 'sababShakwa'

    _rec_name = 'name'
    _order = 'name ASC'

    name = fields.Char(string='سبب الشكوي',required=True,copy=False)
    TicketClassfication=fields.Many2one(comodel_name="ticket.classfication",string="تصنيف الشكوي")
    

class Governates(models.Model):
    _name = 'ewra_governate'
    name=fields.Char(string="name")


# class responsapleparty(models.Model):
#     _name = 'responsapleparty'
#     name=fields.Char(string="Name")
#     serviceintroducer=fields.One2many(string="جهه شكوي",comodel_name="res.partner",inverse_name="responsapleparty")


class ResPartner(models.Model):
    _inherit = 'res.partner'
    # is_complaint = fields.Boolean(string='مقدم خدمة')
    # is_responsable = fields.Boolean(string='الجهة المسئولة')
    companytype=fields.Selection([('complainers','مقدم خدمة'),('responsable ','جهة المسئولة')],string="نوع الشركة")
    
    complainers=fields.One2many(inverse_name="responsables",comodel_name="res.partner",string="مقدم خدمة'")
    responsables=fields.Many2one(string="الجهة المسئولة",comodel_name="res.partner" )
    
   
    
    
    
    #responsapleparty=fields.Many2one(string="Responsable",comodel_name="responsapleparty")
# class serviceintreducer(models.Model):
#     _name = 'serviceintreducer'
#     name=fields.Char(string="Name")
#     responsapleparty=fields.Many2one(string="Responsable",comodel_name="responsapleparty")
    

class ReportingWay(models.Model):
    _name = 'reportingway'
    name=fields.Char("Name")
    

    
    

    
    

    

    
    



    

    
