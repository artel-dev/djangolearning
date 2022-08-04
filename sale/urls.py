from django.urls import path
from . import views

urlpatterns = [
    path("sale", views.sale_index, name="sale-index"),
    path("sale/invoice", views.SaleInvoiceListView.as_view(), name="sale-invoice-list"),
    path("sale/invoice/create", views.SaleInvoiceCreateView.as_view(), name="sale-invoice-create"),
    path("sale/invoice/update/<int:pk>", views.SaleInvoiceUpdateView.as_view(), name="sale-invoice-update"),
    path("sale/invoice/delete/<int:pk>", views.SaleInvoiceDeleteView.as_view(), name="sale-invoice-delete"),
    path("sale/invoice/<int:pk>", views.SaleInvoiceDetailView.as_view(), name="sale-invoice-detail"),
]
