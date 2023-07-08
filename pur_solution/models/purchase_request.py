from odoo import models, fields, api, _


class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'
    name = fields.Char('Reference', default=lambda self: _('New'))

    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed')], default='draft')
    analytical_account_id = fields.Many2one('account.analytic.account', string='Analytical Account')
    create_date = fields.Datetime(string='Creation Date', default=lambda self: fields.Datetime.now(), readonly=True)
    created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user, readonly=True)
    requested_by = fields.Many2one('res.users', string='Requested By', default=lambda self: self.env.user)
    requested_on = fields.Date(string='Requested On', default=fields.Date.context_today)
    purchase_request_lines = fields.One2many('purchase.request.line', 'purchase_request_id',
                                             string='Purchase Request Lines')
    purchase_orders_ids = fields.One2many('purchase.order', 'purshase_request_id')

    # confirm order action
    def button_confirm(self):

        self.ensure_one()
        vendor_lines = {}
        # group by vendor
        for line in self.purchase_request_lines:
            if line.vendor_id not in vendor_lines:
                vendor_lines[line.vendor_id] = self.env['purchase.order.line']
            order_line = self.env['purchase.order.line'].new({
                'name': line.name,
                'product_id': line.product_id.id,
                'product_qty': line.quantity,
                'product_uom': line.product_uom_id,
                'date_planned': fields.Date.today(),
                'price_unit':1.0
            })

            order_line.onchange_product_id()
            vendor_lines[line.vendor_id] += order_line

        for vendor, lines in vendor_lines.items():
            order = self.env['purchase.order'].create({
                'partner_id': vendor.id,
                'order_line': [(0, 0, x._convert_to_write(x._cache)) for x in lines],
            })

            # add created lines
            self.purchase_orders_ids += order

        self.write({'state': 'confirmed'})




    # add refrence after create
    @api.model
    def create(self, vals):

        name = vals.get("name", False)
        if not name:
            vals['name'] = _("New")
        vals['name'] = self.env['ir.sequence'].next_by_code('purchase.request')

        return super(PurchaseRequest, self).create(vals)
