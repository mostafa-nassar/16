from odoo import models, fields,api ,_
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
import base64
from datetime import datetime, date, timedelta, time


class sewage(models.Model):
    _name = 'sewage.water'
    name = fields.Char(string="مياه الصرف الصحي")


class drinking_watter(models.Model):
    _name = 'drinking.water'
    name = fields.Char(string="مياه الشرب")


class commercial(models.Model):
    _name = 'commercial.water'
    name = fields.Char(string="تجاري")


class quality_type(models.Model):
    _name = 'quality.type'
    name = fields.Char()


class complain_issue(models.Model):
    _name = 'complain.issue'

    name = fields.Char(string="تصنيف الشكوي")
    issue_type = fields.Selection(
        [('drinking_water', 'مياه الشرب'), ('sewage', 'مياه الصرف الصحي'), ('commercial', 'تجاريه')],
        string="نوع الشكوي")
    drinking_watter = fields.Many2many('drinking.water', string='مياه الشرب')
    sewage_watter = fields.Many2many('sewage.water', string='مياه الصرف الصحي')
    commercial_watter = fields.Many2many('commercial.water', string='تجاري')
    quality = fields.Boolean(string="جوده")
    billing = fields.Boolean(string="بيانات فواتير")
    # quality_types_ids = fields.Many2many('quality.type',string="جودة المياه")


class helpdesk_custom_portal(models.Model):
    _inherit = 'helpdesk.ticket'

    state_area = fields.Many2one('partner.state.zone', string='المنطقه')
    follower_phone = fields.Char(string='هاتف المتابعه')
    customer_info_name = fields.Char(string='اسم العميل')
    door = fields.Selection([('1', 'الاول'), ('2', 'الثاني'), ('3', 'الثالث')], string='اسم العميل')
    public_street = fields.Char('الشارع العمومي')
    public_street_near = fields.Char('بجوار')
    customer_home_number = fields.Char('رقم المنزل')
    customer_home_address = fields.Char('العنوان')
    identification_number = fields.Char('رقم البطاقه')
    complain_issue_id = fields.Many2one('complain.issue', string="تصنيف الشكوي")
    issue_type = fields.Selection(related='complain_issue_id.issue_type', string='نوع الشكوي', store=True)
    drinking_watter_id = fields.Many2one('drinking.water', string="مياه الشرب")
    sewage_watter_id = fields.Many2one('sewage.water', string="مياه الصرف الصحي")
    commercial_watter_id = fields.Many2one('commercial.water', string="تجاري")

    quality = fields.Boolean(related='complain_issue_id.quality')
    billing = fields.Boolean(related='complain_issue_id.billing')
    water_dark_color = fields.Boolean(string="يوجد لون داكن بالمياه")
    water_bad_smell = fields.Boolean(string="يوجد رائحه كريهه للمياه")
    water_bad_teast = fields.Boolean(string="يوجد طعم سئ بالمياه")
    motor = fields.Boolean(string="يوجد موتور")
    water_safe = fields.Boolean(string="يوجد خزان مياه")
    sup_number = fields.Char(string="رقم الإشتراك")
    zone_number = fields.Char(string="رقم المنطقة")

    complain_source = fields.Selection([('in_door', 'الحضور الشخصى لمركز خدمة المواطنين'),
                                        ('mail', 'البريد العادى'), ('email', 'البريد الإلكترونى'),
                                        ('phone_app', 'تطبيق الهاتف المحمول'), ('whatsup', 'الواتس اب'),
                                        ('facebook', 'الفيس بوك'), ('media', 'وسائل الإعلام'),
                                        ('website', 'الموقغ الالكتروني'),

                                        ], string='مصدر الشكوى')
    procedures = fields.Selection([('mail', 'مراسلة مقدم الخدمة'),
                                   ('check_site', 'معاينة ميدانية'),
                                   ('show_issue', 'العرض على لجنة الشكاوى'),
                                   ('mail_executive', 'مراسلة الجهة التنفيذية'),
                                   ], string='إجراءت المنفذة')


    @api.model
    def create_helpdesk_portal(self, values):
        if not (self.env.user.employee_id):
            raise AccessDenied()
        user = self.env.user
        self = self.sudo()
        if 'complain_issue_id' in values:
            issue_id = self.env['complain.issue'].browse(int(values['complain_issue_id']))
            print(issue_id)
            if issue_id.issue_type == 'drinking_water':
                drinking_water = int(values['issue'])
            else:
                drinking_water = False
            if issue_id.issue_type == 'sewage':
                sewage = int(values['issue'])
            else:
                sewage = False
            if issue_id.issue_type == 'commercial':
                commercial = int(values['issue'])
            else:
                commercial = False

        print('values['']',values['complain_issue_id'],type(values['complain_issue_id']))
        print(values)
        values = {
            'name': 'شكوي'+' '+ values['customer_info_name'] if 'customer_info_name' in values else False,
            'partner_id':values['partner_id'] if 'partner_id' in values else False,
            'state_area': values['state_area'] if 'state_area' in values else False,
            'water_dark_color': values['water_dark_color'] if 'water_dark_color' in values else False,
            'water_bad_smell': values['water_bad_smell'] if 'water_bad_smell' in values else False,
            'water_bad_teast': values['water_bad_teast'] if 'water_bad_teast' in values else False,
            'motor': values['motor'] if 'motor' in values else False,
            'water_safe': values['water_safe'] if 'water_safe' in values else False,
            'follower_phone': values['follower_phone'] if 'follower_phone' in values else False,

            'partner_phone': values['phone'] if 'phone' in values else False,
            'partner_email': values['email'] if 'email' in values else False,
            'customer_info_name': values['customer_info_name'] if 'customer_info_name' in values else False,
            'door': values['door'] if 'door' in values else False,
            'public_street': values['public_street'] if 'public_street' in values else False,
            'public_street_near': values['public_street_near'] if 'public_street_near' in values else False,
            'customer_home_number': values['customer_home_number'] if 'customer_home_number' in values else False,
            'customer_home_address': values['customer_home_address'] if 'customer_home_address' in values else False,
            'identification_number': values['identification_number'] if 'identification_number' in values else False,
            'complain_issue_id': int(values['complain_issue_id']) if 'complain_issue_id' in values else False,

            'drinking_watter_id': drinking_water,
            'sewage_watter_id': sewage,
            'commercial_watter_id':commercial,

            'sup_number': values['sup_number'] if 'sup_number' in values else False,
            'zone_number': values['zone_number'] if 'zone_number' in values else False,
        }

        tmp_issue = self.env['helpdesk.ticket'].sudo().new(values)
        values = tmp_issue._convert_to_write(tmp_issue._cache)
        myissue = self.env['helpdesk.ticket'].sudo().create(values)
        return {
            'id': myissue.id
        }


