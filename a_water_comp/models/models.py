from odoo import models, fields, api


class waterComp(models.Model):
        _name='water.comp'
        _description ='Regulatory Agency for drinking water, sanitation and consumer protection'



        fiscalyear = fields.Many2one('fiscal.year', string='السنه الماليه  ')
        componyName = fields.Many2one('compony_name', string='أسم الشركة  ')

        unit1 = fields.Char(string='متر مكعب' ,readonly='1')
        unit2 = fields.Char(string='مليون م3' ,readonly='1')


        watermajored = fields.Float('كمية المياه المنتجة المقاسة')
        waterunamaj = fields.Float('كمية المياه المنتجة الغير مقاسة')

        resultwater = fields.Float('كمية المياه المنتجة',compute='calcu_sum',store=True)

        waterforsale = fields.Float('كمية المياه المشتراة بغرض البيع')
        wateravilabelforsale= fields.Float('كمية المياه المتاحة للبيع')
        watermatjorper = fields.Float('نسبة كمية الانتاج المقاس من المياه' ,compute='calc0' ,store=True)
        unwatermatjorper = fields.Float('نسبة كمية الانتاج غير المقاس من المياه'  ,compute='calc1' ,store=True)


        surfacestat = fields.Float('محطات سطحية' )
        ertwez = fields.Float(' أبار إرتوازية' )
        sewatst = fields.Float('محطات تحلية مياه بحار ' )
        sum0 = fields.Float('كمية المياه المنتجة' )


        @api.depends('surfacestat','waterunamaj','resultwater')
        def calcu_sum(self):
                for rec in self:
                        rec.resultwater=rec.waterunamaj + rec.watermajored




        @api.depends('watermajored','waterunamaj','resultwater')
        def calcu_sum(self):
                for rec in self:
                        rec.resultwater=rec.waterunamaj + rec.watermajored


        @api.depends('watermajored','resultwater','watermatjorper')
        def calc0(self):
                for rec in self:
                        rec.watermatjorper = rec.watermajored / rec.resultwater

        @api.depends('unwatermatjorper', 'watermatjorper')
        def calc1(self):
                for rec in self:
                        rec.unwatermatjorper = 1 - rec.watermatjorper





        wtareamountfix= fields.Float('كمية المياه المنتجة من المحطات الثابتة')
        wateramountmotile =fields.Float('كمية المياه المنتجة من المحطات النقالى')
        waterErtewazic=fields.Float('كمية المياه المنتجة من المحطات الإرتوازى')
        watersae=fields.Float('كمية المياه المنتجة من محطات تحلية مياه بحار')
        reswater2= fields.Float('كمية المياه المنتجة',compute='calcu_sum2',store=True)

        @api.depends('wtareamountfix', 'wateramountmotile', 'waterErtewazic','watersae','reswater2')
        def calcu_sum2(self):
                for rec in self:
                        rec.reswater2 = rec.wtareamountfix + rec.wateramountmotile +rec.waterErtewazic+rec.watersae









        surfacestat = fields.Float(' نسبة المياه المنتجه  / محطات سطحية' ,compute='calcu_sum00' ,store=True)
        ertwez = fields.Float('نسبة المياه المنتجه  /  أبار إرتوازية', compute='calcu_sum03' ,store=True)
        sewatst = fields.Float(' نسبة المياه المنتجه  / محطات تحلية مياه بحار ' ,compute='calcu_sum02' ,store=True)
        sum0 = fields.Float(' نسبة كمية المياه المنتجة' ,compute='calcu_sum01' ,store=True)


        @api.depends('surfacestat','wtareamountfix','reswater2')
        def calcu_sum00(self):
                for rec in self:
                        rec.surfacestat=rec.wtareamountfix / rec.reswater2



        @api.depends('ertwez','sewatst','surfacestat','sum0')
        def calcu_sum01(self):
                for rec in self:
                        rec.sum0 =rec.sewatst+ rec.ertwez+rec.surfacestat




        @api.depends('sewatst','watersae','reswater2')
        def calcu_sum02(self):
                for rec in self:
                        rec.sewatst=rec.watersae / rec.reswater2





        @api.depends('ertwez','waterErtewazic','reswater2')
        def calcu_sum03(self):
                for rec in self:
                        rec.ertwez=rec.waterErtewazic / rec.reswater2



























        majordsaledwater=fields.Float('كمية المياه المباعة المقاسة')
        unmajordsaledwater=fields.Float('كمية المياه المباعة الغير مقاسة')
        totalsaledwater=fields.Float('إجمالي كمية المياه المباعة'  , compute='calcu_sum3',store=True)

        @api.depends('majordsaledwater', 'unmajordsaledwater', 'totalsaledwater')
        def calcu_sum3(self):
                for rec in self:
                        rec.totalsaledwater = rec.majordsaledwater + rec.unmajordsaledwater

        collecteedsoua=fields.Float('كمية الصرف المجمع ')
        collectedunprocsoa=fields.Float('كمية الصرف المجمع التى تصرف مباشرة على المصارف دون معالجة')
        precesoa=fields.Float('كمية الصرف المعالج (محطات تابعة للشركة)')
        precesoafromagancy=fields.Float('كمية الصرف المعالج (محطات تحت اشراف الهيئة القومية)')





        house_usege = fields.Float(string='منزلى')
        coomer_usege = fields.Float(string='تجارى')
        tour_usege = fields.Float(string='سياحى')
        gove_usege = fields.Float(string='حكومى')
        serv_usege = fields.Float(string='خدمي')
        indus_usege = fields.Float(string='صناعي')
        sports_usege = fields.Float(string='أندية رياضية')
        other_usege = fields.Float(string='أخري')
        total= fields.Float('الاجمالى'   , compute='calcu_sum4',store=True)




        @api.depends('house_usege', 'coomer_usege', 'tour_usege','gove_usege','serv_usege', 'indus_usege','sports_usege', 'other_usege','total')
        def calcu_sum4(self):
                for rec in self:
                        rec.total= rec.house_usege+ rec.coomer_usege+rec.tour_usege+rec.gove_usege+rec.serv_usege+rec.indus_usege+rec.sports_usege+rec.other_usege



        popnum=fields.Float('عدد السكان بالمحافظة')
        citynum=fields.Float('عدد المدن')
        regnum=fields.Float('عدد القرى / المناطق')
        bloknum=fields.Float('عدد العزب')











        pophavwater=fields.Float('عدد السكان المخدومين بمياه الشرب')
        citywithwater=fields.Float('عدد المدن المخدومة بمياه الشرب')
        vlgwithwater=fields.Float('ععدد القرى / المناطق المخدومة بمياه الشرب')
        blockwithwater=fields.Float('عدد العزب المخدومة بمياه الشرب')


        pophavsou=fields.Float('عدد السكان المخدومين بالصرف الصحى')
        citywithsou=fields.Float('عدد المدن المخدومة بالصرف الصحى')
        vlgwithsou=fields.Float('عدد القرى / المناطق المخدومة بالصرف الصحى')
        blockwithsou=fields.Float('عدد العزب المخدومة بالصرف الصحى')


