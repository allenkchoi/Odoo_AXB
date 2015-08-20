from openerp.osv import osv, fields


class SaleOrder(osv.osv):
    _inherit = 'sale.order'
    _columns = {
	'payment_method': fields.many2one('payment.method', 'Payment Method'),

    }
