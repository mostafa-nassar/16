from odoo import models, fields, api


class Cost_percubic (models.Model):
        _name = 'costpercubic.mod'
        _description ='Table- Cost per cubic meter of produced water'
        name= fields.Char('name')

        fiscalyear = fields.Many2one('fiscal.year', string='السنه الماليه  ')
        componyName = fields.Many2one('compony_name', string='أسم الشركة  ')




        workcost = fields.Float('تكلفة العمالة')
        gas = fields.Float('تكلفة الوقود والزيوت')
        electr = fields.Float('تكلفة الكهرباء')
        messi = fields.Float('قطع غيار ومهمات')
        lost = fields.Float('الإهلاك')
        coomer = fields.Float('الفوائد')
        others = fields.Float('تكاليف تشغيلية أخرى')
        lostandcomm = fields.Float('تكلفة التشغيل والصيانة بالإهلاك والفوائد')




        workcost2 = fields.Float('تكلفة العمالة')
        gas2 = fields.Float('تكلفة الوقود والزيوت')
        electr2 = fields.Float('تكلفة الكهرباء')
        messi2 = fields.Float('قطع غيار ومهمات')
        lost2 = fields.Float('الإهلاك')
        coomer2 = fields.Float('الفوائد')
        others2 = fields.Float('تكاليف تشغيلية أخرى')
        lostandcomm2 = fields.Float('تكلفة التشغيل والصيانة بالإهلاك والفوائد')




        workcost3 = fields.Float('تكلفة العمالة')
        gas3 = fields.Float('تكلفة الوقود والزيوت')
        electr3 = fields.Float('تكلفة الكهرباء')
        messi3 = fields.Float('قطع غيار ومهمات')
        lost3 = fields.Float('الإهلاك')
        coomer3 = fields.Float('الفوائد')
        others3 = fields.Float('تكاليف تشغيلية أخرى')
        lostandcomm3 = fields.Float('تكلفة التشغيل والصيانة بالإهلاك والفوائد')



