# -*- coding: utf-8 -*-

from odoo import fields,models,api

class report_account_aged_receivable(models.AbstractModel):
    _inherit = "account.aged.receivable"
    
    filter_operating_units = True

    
    def _build_options(self, previous_options=None):
        options = super(report_account_aged_receivable, self)._build_options(previous_options=previous_options)
        if self.filter_operating_units:
            options['operating_units'] = self._get_operating_units()
            if previous_options and 'operating_units' in previous_options  and options['operating_units'] and previous_options['operating_units'] is not None:
                options['operating_units'] = previous_options['operating_units']
            
        return options
    
    def _get_operating_units(self):
        operating_units_read = self.env['operating.unit'].search([('company_id', 'in', self.env.user.company_ids.ids or [self.env.user.company_id.id])], order="company_id, name")
        operating_units = []
        previous_company = False
        for c in operating_units_read:
            if c.company_id != previous_company:
                operating_units.append({'id': 'divider', 'name': c.company_id.name})
                previous_company = c.company_id
            operating_units.append({'id': c.id, 'name': c.name, 'code': c.code, 'selected': False})
        return operating_units
    
    
    @api.model
    def _get_options(self, previous_options=None):
        options = super(report_account_aged_receivable, self)._get_options(previous_options)
        if options.get('operating_units'):
            filter_operating_units = True
            options['operating_units'] = self._get_operating_units()
            if previous_options and 'operating_units' in previous_options  and options['operating_units'] and previous_options['operating_units'] is not None:
                options['operating_units'] = previous_options['operating_units']
        else:
            filter_operating_units = False
        return options
    
    
class report_account_aged_payable(models.AbstractModel):
    _inherit = "account.aged.payable"
    
    filter_operating_units = True
    
    def _build_options(self, previous_options=None):
        options = super(report_account_aged_payable, self)._build_options(previous_options=previous_options)
        if self.filter_operating_units:
            options['operating_units'] = self._get_operating_units()
            if previous_options and 'operating_units' in previous_options  and options['operating_units'] and previous_options['operating_units'] is not None:
                options['operating_units'] = previous_options['operating_units']
            
        return options
    
    def _get_operating_units(self):
        operating_units_read = self.env['operating.unit'].search([('company_id', 'in', self.env.user.company_ids.ids or [self.env.user.company_id.id])], order="company_id, name")
        operating_units = []
        previous_company = False
        for c in operating_units_read:
            if c.company_id != previous_company:
                operating_units.append({'id': 'divider', 'name': c.company_id.name})
                previous_company = c.company_id
            operating_units.append({'id': c.id, 'name': c.name, 'code': c.code, 'selected': False})
        return operating_units
    

    @api.model
    def _get_options(self, previous_options=None):
        options = super(report_account_aged_payable, self)._get_options(previous_options)
        if options.get('operating_units'):
            filter_operating_units = True
            options['operating_units'] = self._get_operating_units()
            if previous_options and 'operating_units' in previous_options  and options['operating_units'] and previous_options['operating_units'] is not None:
                options['operating_units'] = previous_options['operating_units']
        else:
            filter_operating_units = False
        return options

    
