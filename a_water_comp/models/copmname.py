from odoo import models, fields, api


class compony_name (models.Model):
        _name = 'compony_name'
        _description ='compony name'
        _rec_name = 'name'



        name = fields.Char(string='أسم الشركة ')
