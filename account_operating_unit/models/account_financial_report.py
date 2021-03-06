# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ReportAccountFinancialReport(models.Model):
    _inherit = "account.financial.html.report"
    
    show_operating_units_filter = fields.Boolean('Allow filtering by Operating Units', help='display the Operating units filter in the report')
    filter_operating_units = fields.Boolean('filter_operating_units')
    
    def _build_options(self, previous_options=None):
        options = super(ReportAccountFinancialReport, self)._build_options(previous_options=previous_options)
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
        options = super(ReportAccountFinancialReport, self)._get_options(previous_options)
        if self.show_operating_units_filter:
            self.filter_operating_units = True
            options['operating_units'] = self._get_operating_units()
            if previous_options and 'operating_units' in previous_options  and options['operating_units'] and previous_options['operating_units'] is not None:
                options['operating_units'] = previous_options['operating_units']
        else:
            self.filter_operating_units = False
        return options
    
    @api.model
    def _get_options_domain(self, options):
        # OVERRIDE to handle custom domains by the ir.filter filter.
        domain = super(ReportAccountFinancialReport, self)._get_options_domain(options)
        op_units = options.get('operating_units')
        if op_units:
            op_unit_ids = [unit.get('id') for unit in options.get('operating_units') if unit.get('selected')]
            if op_unit_ids:
                domain += [('operating_unit_id','in',op_unit_ids)]
        return domain
    
    
