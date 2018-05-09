# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Piso(models.Model): 
    _name = 'ej.Piso' 
    numero_piso = fields.Integer(string='numero_local', required=True) 
 
 
