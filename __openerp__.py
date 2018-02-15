# -*- coding: utf-8 -*-

{
    'name': 'Paypal as a Friend Payment Acquirer',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: Paypal as a Friend Implementation',
    'version': '1.0',
    'description': """Paypal as a Friend Payment Acquirer""",
    'website': 'https://github.com/mumaker',
    'depends': ['payment'],
    'data': [
        'views/paypal_friend.xml',
        'data/paypal_friend.xml',
    ],
    'installable': True,
    'auto_install': True,
}
