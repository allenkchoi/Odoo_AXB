from openerp.osv import osv, fields

class AccountInvoice(osv.osv):
    _inherit = 'account.invoice'
    _columns = {
	'sale_order': fields.many2one('sale.order', 'Sale Order', readonly=True),
    }
