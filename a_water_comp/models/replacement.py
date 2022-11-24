from odoo import models, fields, api


class replacement_cost (models.Model):
        _name = 'replacement.cost'
        _description ='Cost of replacement, renewal and new projects'



        fiscalyear = fields.Many2one('fiscal.year', string='السنه الماليه  ')
        componyName = fields.Many2one('compony_name', string='أسم الشركة  ')






        replac = fields.Float('الإحلال والتجديد')
        localspoi = fields.Float('المحليات')

        totalinvpl = fields.Float('إجمالى المنصرف من الخطة الإستثمارية')




        materials = fields.Float('خامات ومواد')
        fuel = fields.Float('وقود')
        oils = fields.Float('زيوت وشحوم')
        chpar = fields.Float('قطع غيار')
        messions = fields.Float('مواد ومهمات')
        weasts = fields.Float('المخلفات والخردة')
        itemsforsales = fields.Float('مشتريات بغرض البيع')
        totalstorepoint = fields.Float('إجمالى رصيد المخزون')



