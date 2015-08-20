from openerp.osv import osv, fields


class PurchaseOrder(osv.osv):
    _inherit = 'purchase.order'
    _columns = {
	'payment_method': fields.many2one('payment.method', 'Payment Method'),

    }
