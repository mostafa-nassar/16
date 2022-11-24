from odoo import models, fields, api


class electricity (models.Model):
        _name = 'electricity.mod'
        _description ='Electricity'



        fiscalyear = fields.Many2one('fiscal.year', string='السنه الماليه  ')
        componyName = fields.Many2one('compony_name', string='أسم الشركة  ')





        unit1=fields.Char('جنيه')
        unit2=fields.Char('كيلوات')
        unit3=fields.Char('%')
        unit4=fields.Char('طن')
        unit5=fields.Char('كيلو متر')


        lastyears = fields.Float('رصيد أول المدة (مديونية الأعوام السابقة)')
        currentyear = fields.Float('المستحق خلال العام (قيمة إستهلاك العام)')
        totalforElctrCom = fields.Float('إجمالي المستحق لصالح شركات الكهرباء')
        recived = fields.Float('المسدد من المستحق لصالح شركات الكهرباء')
        percintcurr = fields.Float('نسبة المسدد إلي المستحق خلال العام (قيمة إستهلاك العام)')
        recivedpercintage = fields.Float('نسبة المسدد إلي إجمالي المستحق لصالح شركات الكهرباء')
        unrecived = fields.Float('رصيد آخر المدة (الغير مسدد من مستحقات شركات الكهرباء)')







        elctforwater = fields.Float('كمية الكهرباء المستهلكة بمياه الشرب')
        solidice = fields.Float('كمية الشبة الصلبة المستهلكة ')
        liquidice = fields.Float('كمية الشبة السائلة المستهلكة ')
        cl_amount = fields.Float('كمية الكلور السائل المستهلكة ')
        cl_solidamount = fields.Float('كمية الكلور البودرة المستهلكة')
        solidice2 = fields.Float('قيمة  الشبة الصلبة المستهلكة ')
        liquidice2 = fields.Float('قيمة  الشبة السائلة المستهلكة ')
        cl_amount2 = fields.Float('قيمة  الكلور السائل المستهلكة ')
        cl_solidamount2 = fields.Float('قيمة  الكلور البودرة المستهلكة')






        elecric_amoumt = fields.Float('كمية الكهرباء المستهلكة')
        cl_amount3 = fields.Float('كمية  الكلور السائل المستهلكة ')
        cl_solidamount3 = fields.Float('كمية  الكلور البودرة المستهلكة')
        elecric_amoumt2 = fields.Float('قيمة الكهرباء المستهلكة ')
        cl_amount4 = fields.Float('قيمة الكلور السائل المستهلكة ')
        cl_solidamount4 = fields.Float('قيمة الكلور البودرة المستهلكة')



        waterdrinknumberfix = fields.Float('عدد محطات مياه الشرب الثابتة')
        waterdrinknumbermotil = fields.Float('عدد محطات مياه الشرب النقالى')
        waterdrinknumberartz = fields.Float('عدد محطات مياه الشرب الأرتوازى')
        waterdrinktall = fields.Float('أطوال شبكات مياه الشرب')
        netstall = fields.Float('أطوال الإحلال والتجديد للشبكات خلال السنة')
        netstallbroken = fields.Float('عدد حالات الكسر والإنفجارات')
        netstallfall = fields.Float('عدد حالات التسربات')





        tripoler = fields.Float('عدد محطات المعالجة الثلاثية')
        bipoler = fields.Float('عدد محطات المعالجة الثنائية')
        tri2 = fields.Float('عدد محطات المعالجة الثلاثية')
        pullst = fields.Float('عدد محطات الرفع')
        souanettal = fields.Float('أطوال شبكات الصرف الصحى')
        renewssouatall = fields.Float('أطوال الإحلال والتجديد للشبكات خلال السنة')
        broksoua = fields.Float('عدد حالات الكسر والإنفجارات')
        souafall = fields.Float('عدد حالات التسربات')
