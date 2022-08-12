from django.urls import path
from . import views

urlpatterns = [
    path("purchase", views.purchase_index, name="purchase-index"),
    path("purchase-orders", views.PurchaseOrderListView.as_view(), name="purchase-orders"),
    path("purchase-orders/create", views.PurchaseOrderCreate.as_view(), name="purchase-orders-create"),
]
