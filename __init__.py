# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Esto elimina todas las ciudades que figuran por defecto
# para agregar los Departamentos de Paraguay en data/res_country_states_data.xml
from odoo import api, fields, models
class ResCountryState(models.Model):
    _inherit = "res.country.state"
    @api.model
    def _auto_init(self):
        res = super(ResCountryState, self)._auto_init()
        self.env.cr.execute("""
            DELETE from res_country_state;
        """)
        return res
