# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo import tools
from odoo.addons import decimal_precision as dp
from odoo.exceptions import AccessError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"


    @api.onchange('product_uom_qty')
    def _compute_product_uom_qty(self):
        if self.product_uom_qty:
        	if self.order_id.tipo == "maquinaria":
        		if self.product_uom_qty > 1:
        			raise AccessError(_('La Ctdad pedida solo debe ser 1 '))

