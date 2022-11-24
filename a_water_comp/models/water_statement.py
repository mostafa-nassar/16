from odoo import models, fields, api


class water_statement (models.Model):
        _name = 'water.statement'
        _description ='Analytical statement of the amount of water sold'
        name= fields.Char('name')


        fiscalyear = fields.Many2one('fiscal.year', string='السنه الماليه  ')
        componyName = fields.Many2one('compony_name', string='أسم الشركة  ')





        house_usege_st = fields.Float(string='منزلى')
        coomer_usege_st = fields.Float(string='تجارى')
        tour_usege_st = fields.Float(string='سياحى')
        gove_usege_st = fields.Float(string='حكومى')
        serv_usege_st = fields.Float(string='خدمي')
        indus_usege_st = fields.Float(string='صناعي')
        sports_usege_st = fields.Float(string='أندية رياضية')
        other_usege_st = fields.Float(string='أخري')

        total_st = fields.Float('الاجمالى')



        house_usege_st2 = fields.Float(string='منزلى')
        coomer_usege_st2 = fields.Float(string='تجارى')
        tour_usege_st2 = fields.Float(string='سياحى')
        gove_usege_st2 = fields.Float(string='حكومى')
        serv_usege_st2 = fields.Float(string='خدمي')
        indus_usege_st2 = fields.Float(string='صناعي')
        sports_usege_st2 = fields.Float(string='أندية رياضية')
        other_usege_st2 = fields.Float(string='أخري')

        total_st2 = fields.Float('الاجمالى')

        house_usege_st3 = fields.Float(string='منزلى')
        coomer_usege_st3 = fields.Float(string='تجارى')
        tour_usege_st3 = fields.Float(string='سياحى')
        gove_usege_st3 = fields.Float(string='حكومى')
        serv_usege_st3 = fields.Float(string='خدمي')
        indus_usege_st3 = fields.Float(string='صناعي')
        sports_usege_st3 = fields.Float(string='أندية رياضية')
        other_usege_st3 = fields.Float(string='أخري')

        total_st3 = fields.Float('الاجمالى')






        house_usege_st4 = fields.Float(string='منزلى')
        coomer_usege_st4 = fields.Float(string='تجارى')
        tour_usege_st4 = fields.Float(string='سياحى')
        gove_usege_st4 = fields.Float(string='حكومى')
        serv_usege_st4 = fields.Float(string='خدمي')
        indus_usege_st4 = fields.Float(string='صناعي')
        sports_usege_st4 = fields.Float(string='أندية رياضية')
        other_usege_st4 = fields.Float(string='أخري')

        total_st4 = fields.Float('الاجمالى')








        house_usege_st5 = fields.Float(string='منزلى')
        coomer_usege_st5 = fields.Float(string='تجارى')
        tour_usege_st5 = fields.Float(string='سياحى')
        gove_usege_st5 = fields.Float(string='حكومى')
        serv_usege_st5 = fields.Float(string='خدمي')
        indus_usege_st5 = fields.Float(string='صناعي')
        sports_usege_st5 = fields.Float(string='أندية رياضية')
        other_usege_st5 = fields.Float(string='أخري')

        total_st5 = fields.Float('الاجمالى')










        house_usege_st6 = fields.Float(string='منزلى')
        coomer_usege_st6 = fields.Float(string='تجارى')
        tour_usege_st6 = fields.Float(string='سياحى')
        gove_usege_st6 = fields.Float(string='حكومى')
        serv_usege_st6 = fields.Float(string='خدمي')
        indus_usege_st6 = fields.Float(string='صناعي')
        sports_usege_st6 = fields.Float(string='أندية رياضية')
        other_usege_st6 = fields.Float(string='أخري')

        total_st6 = fields.Float('الاجمالى')











        house_usege_st7 = fields.Float(string='منزلى')
        coomer_usege_st7 = fields.Float(string='تجارى')
        tour_usege_st7 = fields.Float(string='سياحى')
        gove_usege_st7 = fields.Float(string='حكومى')
        serv_usege_st7 = fields.Float(string='خدمي')
        indus_usege_st7= fields.Float(string='صناعي')
        sports_usege_st7 = fields.Float(string='أندية رياضية')
        other_usege_st7 = fields.Float(string='أخري')

        total_st7 = fields.Float('الاجمالى')




        act_members = fields.Float('عدد المشتركين الذين يتم محاسبتهم وفقاً لإستهلاكات فعلية')
        avg_members = fields.Float('عدد المشتركين الذين يتم محاسبتهم  وفقاً لمتوسطات تقديرية')



