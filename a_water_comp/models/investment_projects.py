from odoo import models, fields


class investment_projects(models.Model):
    _name = 'investment.projects'




    child_field_ids = fields.One2many('child.model', 'parent_field_id', string="1- المشروعات الإستثمارية لمياه الشرب _ الإنشاءات الجديدة والتوسعات التى دخلت الخدمة خلال العام")


    child_field_ids2 = fields.One2many('child.model2', 'parent_field_id2', string="2- المشروعات الإستثمارية للصرف الصحى")


class ChildModel(models.Model):
    _name = 'child.model'




    child_field_1 = fields.Char(string="الاسم")
    child_field_2 = fields.Char(string="التوصيف")
    child_field_3 = fields.Char(string="جهةالتمويل")
    child_field_4 = fields.Integer(string="التكلفة")
    child_field_5 = fields.Date(string="التاريخ")
    child_field_7= fields.Integer(string="الاطوال")
    child_field_9= fields.Integer(string="عددالمخدومين")
    child_field_6= fields.Char(string="الطاقه")
    child_field_8= fields.Char(string="الجهة المشغلة")

    parent_field_id = fields.Many2one('investment.projects', string="Parent ID")





class ChildModel2(models.Model):
    _name = 'child.model2'


    child_field_11 = fields.Char(string="الاسم")
    child_field_22 = fields.Char(string="التوصيف")
    child_field_33 = fields.Char(string="جهةالتمويل")
    child_field_44 = fields.Integer(string="التكلفة")
    child_field_55 = fields.Date(string="التاريخ")
    child_field_77= fields.Integer(string="الاطوال")
    child_field_99= fields.Integer(string="عددالمخدومين")
    child_field_66= fields.Char(string="الطاقه")
    child_field_88= fields.Char(string="الجهة المشغلة")

    parent_field_id2 = fields.Many2one('investment.projects', string="Parent ID")