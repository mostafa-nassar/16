from odoo import models, fields, api


class fiscalYear (models.Model):
        _name = 'fiscal.year'
        _description ='fiscal.year'


        name = fields.Integer(string='السنه الماليه : ')
