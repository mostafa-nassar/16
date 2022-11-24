from odoo import models, fields, api


class staff_number (models.Model):
        _name = 'staff.number'
        _description ='staff number'





        fiscalyear = fields.Many2one('fiscal.year', string='السنه الماليه  ')
        componyName = fields.Many2one('compony_name', string='أسم الشركة  ')





        stafperfixst=fields.Float('عدد العاملين بالمحطات الثابتة')
        stafpermotst=fields.Float('عدد العاملين بالمحطات النقالى')
        stafpererzst=fields.Float('عدد العاملين بالمحطات الارتوازى')
        stafpernetsst=fields.Float('عدد العاملين بالشبكات والروافع')



        staffperproc=fields.Float('عدد العاملين بمحطات المعالجة')
        staffpernets=fields.Float('عدد العاملين بالشبكات والروافع')


        staffperglo=fields.Float('عدد العاملين بالديوان العام')

        total=fields.Float('إجمالى عدد العاملين بالشركة',compute='calcu_sum')



        @api.depends('stafperfixst','stafpermotst','stafpererzst','stafpernetsst','staffperproc','staffpernets','staffperglo','total')
        def calcu_sum(self):
                for rec in self:
                        rec.total=rec.stafperfixst + rec.stafpermotst+rec.stafpererzst+rec.stafpernetsst+rec.staffperproc+rec.staffpernets+rec.staffperglo





        staffscin=fields.Float('عدد العاملين بتخصصات هندسة وعلوم')
        staffcomm=fields.Float('عدد العاملين بتخصصات تجارة وتنمية إدارية وقانونية')
        stafftech=fields.Float('عدد العاملين بتخصصات فنية وحرفية')
        staffothers=fields.Float('عدد العاملين بتخصصات مكتبية ,خدمات معاونة ,امن واخرى')



        total2=fields.Float( 'إجمالى عدد العاملين بالشركة'  ,compute='calcu_sum2')



        @api.depends('staffscin','staffcomm','stafftech','staffothers','total2')
        def calcu_sum2(self):
                for rec in self:
                        rec.total2=rec.staffscin + rec.staffcomm+rec.stafftech+rec.staffothers

