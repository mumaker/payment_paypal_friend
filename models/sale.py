from openerp import api, fields, models, _

import logging
import pprint

_logger = logging.getLogger(__name__)

class sale_order_extend(models.Model):
	_inherit = 'sale.order'

# Modify payment transaction status when quotation is confirmed manually (Wire Transfer and Paypal as a Friend)
	@api.multi
	def action_confirm(self):
		if self.payment_acquirer_id.name in ["Paypal as a Friend", "Wire Transfer"]:
			tx = self.env['payment.transaction'].search([('id', '=', self.payment_tx_id.id)], limit=1)
			tx.state = 'done'
			#_logger.info('Modify payment transaction to DONE status')

		return super(sale_order_extend,self).action_confirm()