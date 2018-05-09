# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2017 Christian Sanchez
#    (<http://www.christian.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Alquileres',
    'version': '1.0',
    'author': "Ing. Christian S�nchez Zeled�n",
    'maintainer': 'Christian S�nchez',
    'website': 'http://www.ChristianSZ.com',
    'license': 'AGPL-3',
    'category': 'account.payment',
    'summary': 'Modulo de Alquileres',
    'depends': ['account','account_accountant'],
    'description': """
Modulo basado en Odoo
===================================================== 
�ste m�dulo permite selecionar 
""",
    'demo': [],
    'test': [],
    'data': ['views/Local_view.xml','views/Alquiler_view.xml','views/Edificio_view.xml','views/Piso_view.xml'],
    'installable': True,
    'auto_install': False,
}
