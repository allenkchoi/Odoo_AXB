# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Serpent Consulting Services PVT. LTD. (<http://www.serpentcs.com>) 
#    Copyright (C) 2011 NovaPoint Group LLC (<http://www.novapointgroup.com>)
#    Copyright (C) 2004-2010 OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################
import openerp.addons.decimal_precision as dp
from openerp.osv import fields, osv

class stock_move(osv.osv):
    _inherit = "stock.move"

    _columns = {
        'package_id' : fields.many2one('stock.packages', help='Indicates the package', string='Package'),
        'cost': fields.float('Value', digits_compute=dp.get_precision('Account'))
    }
    
    def onchange_quantity(self, cr, uid, ids, product_id, product_qty, product_uom, product_uos, location_id=False, sale_line_id=False):
        result = super(stock_move, self).onchange_quantity(cr, uid, ids, product_id, product_qty, product_uom, product_uos)
        if product_id:
            product = self.pool.get('product.product').browse(cr, uid, product_id)
            if sale_line_id:
                sale_unit_price = self.pool.get('sale.order.line').browse(cr, uid, sale_line_id).price_unit
                price = sale_unit_price * product_qty
            else:
                price = product.list_price * product_qty
            result['value'].update({'cost': price})
        return result
    
stock_move()