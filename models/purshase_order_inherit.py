
from odoo import models, fields,api



class purshaseOrderInherit(models.Model):
    _inherit='purchase.order'
    purshase_request_id= fields.Many2one('purchase.request')

    def open_one2many_line(self):
        return {

            'type': 'ir.actions.act_window',

            'name': 'Model Title',

            'view_type': 'form',

            'view_mode': 'form',

            'res_model': self._name,

            'res_id': self.id,

            'target': 'current',

        }


