import string

from odoo import models, fields, api

class PartnerDeliveryZone(models.Model):
    _name = "partner.state.zone"
    _description = "Partner State zone"

    code = fields.Char()
    name = fields.Char(string="Area", required=True)
    active = fields.Boolean(default=True)
    state = fields.Many2one(
        'res.country.state', string='State', store=True,
    )
    country = fields.Many2one(related='state.country_id')
    _sql_constraints = [
        ('name_uniq', 'unique (name)',
         'The name of the Area must be unique !'),
        ('code_uniq', 'unique (code)',
         'The code of the Area must be unique !')
    ]
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        if args is None:
            args = []

        ids = []
        if len(name) == 2:
            ids = list(self._search([('code', 'ilike', name)] + args, limit=limit))

        search_domain = [('name', operator, name)]
        if ids:
            search_domain.append(('id', 'not in', ids))
        ids += list(self._search(search_domain + args, limit=limit))

        return ids

class ResPartner(models.Model):
    _inherit = 'res.partner'
    is_complaint = fields.Boolean(string='جهه شكوي')
    state_area = fields.Many2one('partner.state.zone',string='المنطقه')