from odoo import models, fields, api


class fiscalYear (models.Model):
        _name = 'fiscal.year'
        _description ='fiscal.year'


        name = fields.Char(string='السنه الماليه : ')
