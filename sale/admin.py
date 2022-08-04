from django.contrib import admin
from .models import SaleInvoice, SaleInvoiceLine

# Register your models here.

admin.site.register(SaleInvoice)
admin.site.register(SaleInvoiceLine)
