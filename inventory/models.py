
from django.db import models
from references.models import User, Product, Company  #Warehouse


class PickAndPack(models.Model):
    date = models.DateTimeField()
    number = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="pick_invoices")
    # warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="pick_invoices")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pick_invoices")

    def __str__(self):
        return f"Pick and pack {self.number} ({self.date})"


class PickAndPackLine(models.Model):
    pick_and_pack = models.ForeignKey(PickAndPack, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="pick_and_pack_lines")
    # description = models.CharField(max_length=150)
    qty = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        #return f"{self.product}-{self.description} ({self.pick_and_pack})"
        return f"{self.product} ({self.sale_invoice})"
