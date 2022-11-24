from odoo import models, fields, api


class collection_table (models.Model):
        _name = 'collection.table'
        _description ='Collection rates input tables'
        name = fields.Char('name')


        fiscalyear = fields.Many2one('fiscal.year', string='السنه الماليه  ')
        componyName = fields.Many2one('compony_name', string='أسم الشركة  ')





        stafperfixst=fields.Float('عدد العاملين بالمحطات الثابتة')












        #
        #
        # @api.depends('stafperfixst','stafpermotst','stafpererzst','stafpernetsst','staffperproc','staffpernets','staffperglo','total')
        # def calcu_sum(self):
        #         for rec in self:
        #                 rec.total=rec.stafperfixst + rec.stafpermotst+rec.stafpererzst+rec.stafpernetsst+rec.staffperproc+rec.staffpernets+rec.staffperglo
        #

