from odoo import api, fields, models, tools, _
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):

    _inherit = 'product.template'


    in_home = fields.Boolean(string="Display product in homepage")
    description_title_product = fields.Text(string="Product Description Title")
    description_product = fields.Text(string="Product Description")
    itinirary = fields.Text(string="Itinirary")
    deal_price = fields.Float(string="Deal Price")
    bool_deal_price = fields.Boolean(default=False)



    @api.onchange('public_categ_ids')
    def public_category_ids(self):
        _logger.warning('|- _______ -|- _________ -|')
        deal = self.env.ref('bluebaydive_theme.product_category_public_deals').id
        _logger.warning(deal)
        _logger.warning(self.public_categ_ids)
        categories =[]
        for rec in self.public_categ_ids:
            _logger.warning(rec._origin.id)
            categories.append(rec._origin.id)
        if deal in categories:
            self.write({
                    'bool_deal_price':True,
                    })
        else :
            self.write({
                        'bool_deal_price':False,
                        'deal_price':0,
                        })



    
class Website(models.Model):
    _inherit = "website"
    


    shop_ppg = fields.Integer(default=21, string="Number of products in the grid on the shop")
    shop_ppr = fields.Integer(default=3, string="Number of grid columns on the shop")

    @api.model
    def get_tour_trips_categories(self):
        tour_trips = self.env.ref('bluebaydive_theme.product_category_public_tour_trips').id
        category_ids = self.env['product.public.category'].search(
            [('parent_id', '=', tour_trips)])
        res = {
            'tour_trips': category_ids,
        }
        return res

    @api.model
    def get_cura_diving_categories(self):
        curacao_diving = self.env.ref('bluebaydive_theme.product_category_curacao_diving').id
        category_ids = self.env['product.public.category'].search(
            [('parent_id', '=', curacao_diving)])
        res = {
            'curacao_diving': category_ids,
        }
        return res

