from django.db import models
from references.models import User, Partner, Product


class PurchaseOrder(models.Model):
    date = models.DateTimeField()
    number = models.CharField(max_length=20)
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="purchase_order")
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True, default=None, related_name="purchase_order")
    # warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="purchase_order")
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="purchase_order")

    def __str__(self):
        return f"Purchase Order {self.number} ({self.date})"


class PurchaseOrderLine(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="purchase_order_lines")
    qty = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.product}-{self.price} ({self.purchase_order})"
