# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO Open Source Management Solution
#
#    ODOO Addon module by Uncanny Consulting Services LLP
#    Copyright (C) 2024 Uncanny Consulting Services LLP (<https://uncannycs.com>).
#
##############################################################################
{
    "name": "Hospital Ucs",
    "version": "17.0.1.0.0",
    "website": "https://uncannycs.com",
    "author": "Uncanny Consulting Services LLP",
    "maintainers": "Uncanny Consulting Services LLP",
    "license": "Other proprietary",
    "category": "Extra Tools",
    "summary": "Basic Module",
    "description": """""",
    "depends": [
        'base', 'sale'
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hospital.xml",
        "views/patient.xml"
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
