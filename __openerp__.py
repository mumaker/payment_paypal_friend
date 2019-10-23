# -*- coding: utf-8 -*-

{
    'name': 'Paypal as a Friend Payment Acquirer',
    'author':'mumaker',
    'category': 'Accounting',
    'summary': 'Payment Acquirer: Paypal as a Friend Implementation',
    'version': '1.0',
    'description': """Paypal as a Friend Payment Acquirer
    201910
    It includes changing status in transaction payment when quotation is confirm/cancell/draft manually.
    This changing will afect wire transfer and paypal as a friend payment acquirer and they need to select
    'At payment with acquirer confirmation' option in Order Confirmation field in Payment Acquirer Configuration.

    """,
    'website': 'https://github.com/vandekul',
    'depends': ['payment', 'sale'],
    'data': [
        'views/paypal_friend.xml',
        'data/paypal_friend.xml',
    ],
    'installable': True,
    'auto_install': True,
}
