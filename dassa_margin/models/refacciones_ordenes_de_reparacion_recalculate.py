# Copyright 2014 Carlos Sánchez Cifuentes <csanchez@grupovermon.com>
# Copyright 2015 Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
# Copyright 2015 Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>
# Copyright 2016 Vicent Cubells <vicent.cubells@tecnativa.com>
# Copyright 2017 David Vidal <david.vidal@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models
from odoo import tools
import math


class RefaccionesOrdenesDeReparacion(models.Model):
    _inherit = 'refacciones.ordenes.de.reparacion'

    event_ticket_id = fields.Many2one('event.event.ticket', string='Event Ticket', help="Choose "
        "an event ticket and it will automatically create a registration for this event ticket.")

    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        if not self.event_ticket_id:
            super(RefaccionesOrdenesDeReparacion, self).product_uom_change()