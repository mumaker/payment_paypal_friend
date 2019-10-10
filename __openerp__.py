# -*- coding: utf-8 -*-

{
    'name': 'Paypal as a Friend Payment Acquirer',
    'author':'mumaker',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: Paypal as a Friend Implementation',
    'version': '1.0',
    'description': """Paypal as a Friend Payment Acquirer
    20191010 - It includes changing status in transaction payment when quotation is confirm manually
    """,
    'website': 'https://github.com/mumaker',
    'depends': ['payment', 'sale'],
    'data': [
        'views/paypal_friend.xml',
        'data/paypal_friend.xml',
    ],
    'installable': True,
    'auto_install': True,
}
