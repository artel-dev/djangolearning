from django.forms import ModelForm, inlineformset_factory
from .models import SaleInvoice, SaleInvoiceLine


class SaleInvoiceForm(ModelForm):
    class Meta:
        model = SaleInvoice
        fields = "__all__"


class SaleInvoiceLineForm(ModelForm):
    class Meta:
        model = SaleInvoiceLine
        fields = "__all__"


sale_invoice_formset = inlineformset_factory(SaleInvoice, SaleInvoiceLine, fields="__all__")
