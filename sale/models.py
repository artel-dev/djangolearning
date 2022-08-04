from django.db import models
from references.models import User, Partner, Product


class SaleInvoice(models.Model):
    date = models.DateTimeField()
    number = models.CharField(max_length=20)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="sale_invoices")
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True, default=None, related_name="sale_invoices")
    # warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="sale_invoices")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sale_invoices")

    def __str__(self):
        return f"Sale invoice {self.number} ({self.date})"


class SaleInvoiceLine(models.Model):
    sale_invoice = models.ForeignKey(SaleInvoice, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="sale_invoice_lines")
    description = models.CharField(max_length=150)
    qty = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.product}-{self.description} ({self.sale_invoice})"
