
from odoo import http

from odoo.http import request
from odoo.addons.web.controllers import main

class Home(main.Home):

    @http.route(website=True, auth="public", sitemap=False)
    def web_login(self, *args, **kw):
        res=super(Home, self).web_login(*args, **kw)
        account=request.session.uid
        user=request.env['res.users'].search([('id','=',account)])
        if user.parent_id:
            parent=user.parent_id
            usertype=parent.companytype
            userid=parent.id
        else:
            usertype=user.partner_id.companytype
            userid=user.partner_id.id
        if usertype:
            request.session['usertype']=usertype
        request.session['customerewra']=userid        
        return res    
