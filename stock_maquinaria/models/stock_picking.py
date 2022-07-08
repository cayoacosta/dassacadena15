# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import UserError
from lxml import etree

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    tipo = fields.Selection([('refacciones','Refacciones'),('maquinaria','Maquinaria'),('taller','Taller')],
    	string='Tipo',default='refacciones')

    @api.onchange('tipo')
    def _condicionar_tipo(self):
        domain = {}

        if self.tipo == 'maquinaria':
            domain = {'picking_type_id':[('maq_ref','=',True)]}
            return {'domain' : domain}
        else:
            domain = {'picking_type_id':[('maq_ref','=',False)]}
            return {'domain' : domain}

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            seq_code = 'stock.picking'
            if vals.get('tipo','')=='refacciones':
                seq_code = 'stock.picking.refacciones'
            elif vals.get('tipo','')=='maquinaria':
                seq_code = 'stock.picking.maquinaria'
                
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code(seq_code) or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code(seq_code) or _('New')
        result = super(StockPicking, self).create(vals)
        return result

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(StockPicking, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            tipo = self._context.get('default_tipo','')
            if not tipo:
                tipo = 'refacciones' 
            
            doc = etree.XML(res['fields']['move_ids_without_package']['views']['tree']['arch'])
            for node in doc.xpath("//field[@name='product_id']"):
                node.set('domain', "[('tipo_de_venta', '=', '%s')]"%(tipo))
            res['fields']['move_ids_without_package']['views']['tree']['arch'] = etree.tostring(doc)
            
            doc = etree.XML(res['fields']['move_ids_without_package']['views']['tree']['arch'])
            for node in doc.xpath("//field[@name='product_id']"):
                node.set('domain', "[('tipo_de_venta', '=', '%s')]"%(tipo))
            res['fields']['move_ids_without_package']['views']['tree']['arch'] = etree.tostring(doc)
            
        return res


