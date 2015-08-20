{
    'name': 'Payment Method',
    'version': '1.1',
    'author': 'Kyle Waid',
    'category': 'Sales Management',
    'depends': ['account', 'sale', 'purchase'],
    'website': 'https://www.gcotech.com',
    'description': """ 
    """,
    'data': ['views/sale.xml',
	     'views/payment_method.xml',
	     'views/account_invoice.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}
