from django.forms import ModelForm, inlineformset_factory
from .models import PurchaseOrder, PurchaseOrderLine


class PurchaseOrderForm(ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['date', 'number', 'partner']


class PurchaseOrderLineForm(ModelForm):
    class Meta:
        model = PurchaseOrderLine
        fields = "__all__"


purchase_order_formset = inlineformset_factory(PurchaseOrder, PurchaseOrderLine, fields=['purchase_order'])
