# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class Alquiler(models.Model): 
    _name = 'ej.Alquiler' 
    numero_contrato = fields.Integer(string='numero_contrato', required=True) 
 
    locales_alquilados = fields.Integer(string='locales_alquilados', required=True) 
 
    monto_mensual = fields.Integer(string='monto_mensual', required=True) 
 
    mantenimiento = fields.Integer(string='mantenimiento', required=True) 
 
    facturas_emitidas = fields.Integer(string='facturas_emitidas', required=True) 
 
    fecha_inicio = fields.Datetime(string='fecha_inicio', required=True) 

    fecha_final = fields.Datetime(string='fecha_final', required=True) 
 
