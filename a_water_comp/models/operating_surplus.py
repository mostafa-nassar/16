from odoo import models, fields, api


class operating_surplus (models.Model):
        _name = 'operating.surplus'
        _description ='operating surplus/deficit'


        fiscalyear = fields.Many2one('fiscal.year', string='السنه الماليه  ')
        componyName = fields.Many2one('compony_name', string='أسم الشركة  ')










        watersals = fields.Float('قيمة مبيعات المياه ')
        servtime = fields.Float('إستدامة خدمة')
        itemsforsale = fields.Float('مبيعات بضائع مشتراة بغرض البيع')
        other = fields.Float('إيرادات تشغيلية أخرى')

        totalSal = fields.Float('إجمالى إيرادات التشغيل' ,compute='calcu_sum',store=True)

        @api.depends('watersals','servtime','itemsforsale','other','totalSal')
        def calcu_sum(self):
                for rec in self:
                        rec.totalSal=rec.watersals + rec.servtime+rec.itemsforsale+rec.other





        subl = fields.Float('المنح والاعانات')
        taxesS = fields.Float('إيرادات إستثمارات وفوائد')
        prevtaxesS = fields.Float('إيرادات سنوات سابقة')
        doneappoi = fields.Float('مخصصات انتفى الغرض منها')
        unusi = fields.Float('إيرادات غير عادية')
        otherusi = fields.Float('إيرادات أخرى غير تشغيلية')

        totalusi =fields.Float('إجمالى الإيرادات الكلية')






        workers =fields.Float('تكلفة العمالة')
        oils =fields.Float('تكلفة الوقود والزيوت')
        electr =fields.Float('تكلفة الكهرباء')
        messsions =fields.Float('قطع غيار ومهمات')
        droped =fields.Float('الإهلاك ')
        comm =fields.Float('الفوائد')
        othersWO =fields.Float('تكاليف تشغيلية أخرى')

        totalwork =fields.Float('تكاليف التشغيل والصيانة')






        WoterForSale =fields.Float('مياه مشتراة بغرض البيع')
        itemsforsale =fields.Float('بضائع مشتراة بغرض البيع')
        totalItems =fields.Float('جملة المشتريات بغرض البيع')



        Fordrpo = fields.Float('مخصصات بخلاف الاهلاك')
        unugualloses = fields.Float('خسائر غير عادية')
        prevyears = fields.Float('مصروفات سنوات سابقة')
        othersloses = fields.Float('أعباء وخسائر أخرى')

        totlalos = fields.Float('جملة الأعباء والخسائر')

        totlalspend = fields.Float('إجمالى التكاليف والمصروفات')

# //////////////////////////////// for soua


        souasals = fields.Float('قيمة الصرف الصحي')
        servtimesoua = fields.Float('إستدامة خدمة')
        itemsforsalesua = fields.Float('مبيعات بضائع مشتراة بغرض البيع')
        othersoua = fields.Float('إيرادات تشغيلية أخرى')

        totalSalsoa = fields.Float('إجمالى إيرادات التشغيل')

        sublsoua = fields.Float('المنح والاعانات')
        taxesSsou = fields.Float('إيرادات إستثمارات وفوائد')
        prevtaxesSsoua = fields.Float('إيرادات سنوات سابقة')
        doneappoisoua = fields.Float('مخصصات انتفى الغرض منها')
        unusisou = fields.Float('إيرادات غير عادية')
        otherusisou = fields.Float('إيرادات أخرى غير تشغيلية')

        totalusisou =fields.Float('إجمالى الإيرادات الكلية')






        workerssoua =fields.Float('تكلفة العمالة')
        oilssou =fields.Float('تكلفة الوقود والزيوت')
        electrsoua =fields.Float('تكلفة الكهرباء')
        messsionssoua =fields.Float('قطع غيار ومهمات')
        dropedsoua =fields.Float('الإهلاك ')
        commsoua =fields.Float('الفوائد')
        othersWOsoua =fields.Float('تكاليف تشغيلية أخرى')

        totalworksoua =fields.Float('تكاليف التشغيل والصيانة')






        itemsforsalesoau =fields.Float('بضائع مشتراة بغرض البيع')
        totalItemssoua =fields.Float('جملة المشتريات بغرض البيع')



        Fordrposoua = fields.Float('مخصصات بخلاف الاهلاك')
        unuguallosessoua = fields.Float('خسائر غير عادية')
        prevyearssoua = fields.Float('مصروفات سنوات سابقة')
        otherslosessoua = fields.Float('أعباء وخسائر أخرى')

        totlalossoa = fields.Float('جملة الأعباء والخسائر')

        totlalspendsoua = fields.Float('إجمالى التكاليف والمصروفات')












