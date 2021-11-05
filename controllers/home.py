from odoo.addons.portal.controllers.web import Home
from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)

class WebsiteSort(Home):

    @http.route()
    def index(self, **kw):

      super(WebsiteSort, self).index()
      website_product_ids = request.env['product.template'].search(['&',('is_published', '=', True),('in_home', '=', True)])
      _logger.warning('=========================================')
      _logger.warning(website_product_ids)
      return request.render('website.homepage', {
         'website_product_ids': website_product_ids,
      })

class Dealsclass(http.Controller):

    @http.route('/deals',type='http', auth='public', website=True, sitemap=True)
    def index(self, **kw):
      product_ids = []
      product = request.env['product.template']
      deal = product.env.ref('bluebaydive_theme.product_category_public_deals').id
      public_product_ids = request.env['product.template'].search([('is_published', '=', True)])
      for product in public_product_ids:
        for category in product.public_categ_ids:
          if category.id == deal:
            product_ids.append(product)
      _logger.warning('=========================================')
      _logger.warning(product_ids)
      return http.request.render('bluebaydive_theme.deals',
        {
         'product_ids': product_ids,
      }
      )