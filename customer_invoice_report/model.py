from odoo import models, fields, api
import base64
import qrcode
from io import BytesIO

class CustomerInvoiceReport(models.AbstractModel):
    _name = 'report.customer_invoice_report.invoice_order'
    _description = "Customer Invoice Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        records = self.env['account.move'].browse(docids)

        if records.company_id:
            company = records.company_id
        else:
            company = self.env['res.company'].search([], limit=1)
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': records,
			'company': company
        }

class CustomerInvoiceReport2(models.AbstractModel):
    _name = 'report.customer_invoice_report.invoice_installment_order'
    _description = "Customer Invoice Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        records = self.env['account.move'].browse(docids)

        if records.company_id:
            company = records.company_id
        else:
            company = self.env['res.company'].search([], limit=1)
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': records,
			'company': company
        }




class AccountMove(models.Model):
    _inherit = 'account.move'

    x_invoice_reference = fields.Char(string="Amount Due With VAT In%")


    zatca_qr_image = fields.Binary(
        string='ZATCA QR Code',
        compute='_compute_zatca_qr_image',
        store=False
    )

    @api.depends('l10n_sa_qr_code_str')
    def _compute_zatca_qr_image(self):
        for record in self:
            record.zatca_qr_image = False

            qr_content = record.l10n_sa_qr_code_str
            if not qr_content:
                continue

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_content)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format="PNG")

            # ✅ Correct: Binary expects BASE64 BYTES
            record.zatca_qr_image = base64.b64encode(buffer.getvalue())
            buffer.close()