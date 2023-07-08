from odoo import models, fields,api

class PurchaseRequestLine(models.Model):
    _inherit = 'purchase.order.line'
    _name = 'purchase.request.line'
    _description = 'Purchase Request Line'
    name=fields.Char(string="Description")
    product_id = fields.Many2one('product.product', string='Product')
    vendor_id = fields.Many2one('res.partner', string='Vendor')
    quantity = fields.Float(string='Quantity')
    product_uom_id = fields.Many2one('uom.uom', string='Unit of Measure', domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id')
    purchase_request_id = fields.Many2one('purchase.request', string='Purchase Request')



    def _get_default_description(self):

        if not self.product_id:
            self.name=None

        else:
            self.name= self.product_id.name






    @api.onchange('product_id')
    def _product_id_change(self):
        # clear when no product selected
        if not self.product_id:
            self.vendor_id =None
            self.product_uom_id = None
            self.quantity = None


        self._get_default_description()






