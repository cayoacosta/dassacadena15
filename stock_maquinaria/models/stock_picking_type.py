# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from lxml import etree

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'
    
    maq_ref = fields.Boolean(string="Es Maquinaria", default=False)
    