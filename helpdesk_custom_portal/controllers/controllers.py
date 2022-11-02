from odoo import http
from odoo.http import request


class WebsiteHelpdesk_portal(http.Controller):

    @http.route('''/ewra-helpdesk''', type='http', auth="user", website=True,
                sitemap=True)
    def website_helpdesk_view(self, **kwargs):
        partners = request.env['res.partner'].search([('is_complaint','=',True)])
        issues = request.env['complain.issue'].search([])
        drinking_watters = request.env['drinking.water'].search([])

        return request.render("helpdesk_custom_portal.helpdesk_complain_submit"
                              , {
                                'partners': partners,
                                'issues': issues,
                                'types': drinking_watters,
                              }
                              )

