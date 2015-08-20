from openerp.osv import osv, fields


class PaymentMethod(osv.osv):
    _name = 'payment.method'
    _columns = {
	'name': fields.char('Name'),
	'journal': fields.many2one('account.journal', 'Payment Journal', domain=[('type', 'in', ['bank', 'cash'])]),

    }


