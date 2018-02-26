# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2017 Rapidsoft - http://www.rapidsoft.com.py

{
    'name': 'Paraguay - Accounting',
    'version': '2.0',
    'author': ['Rapidsoft'],
    'website': 'http://www.rapidsoft.com.py',
    'category': 'Localization',
    'depends': ['base', 'account','account_parent'],
    'data':[
        'data/l10n_py_chart_data.xml',
        'data/account_tax_data.xml',
        'data/res_country_states_data.xml',
        'views/res_partner_vat_views.xml',
        'data/account_chart_template_data.yml',
    ],
}
