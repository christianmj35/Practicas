# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Local(models.Model): 
    _name = 'ej.Local' 
    numero_local = fields.Integer(string='numero_local', required=True) 
 
    area = fields.Char(string='area', required=True) 
 
    medidor_electrico = fields.Integer(string='medidor_electrico', required=True) 
 
    medidor_agua = fields.Integer(string='medidor_agua', required=True) 
 
    piso = fields.Integer(string='piso', required=True) 
 
    edificio = fields.Integer(string='edificio', required=True) 
 
