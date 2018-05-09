# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Edificio(models.Model): 
    _name = 'ej.Edificio' 
    nombre = fields.Char(string='nombre', required=True) 
 
    direccion = fields.Char(string='direccion', required=True) 
 
    area_terreno = fields.Integer(string='area_terreno', required=True) 
 
    area_construccion = fields.Integer(string='area_construccion', required=True) 
 
    lista_pisos = fields.Integer(string='lista_pisos', required=True) 
 
    valor_real = fields.Integer(string='valor_real', required=True)

    valor_fiscal = fields.Integer(string='valor_fiscal', required=True)
 
