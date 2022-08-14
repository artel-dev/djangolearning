from django.urls import path
from . import views

urlpatterns = [
    path("inventory", views.inventory_index, name="inventory-index"),
    path("inventory/pick", views.PickAndPackListView.as_view(), name="pick-list"),
    path("inventory/pick/create", views.PickAndPackCreateView.as_view(), name="pick-create"),
    path("inventory/pick/update/<int:pk>", views.PickAndPackUpdateView.as_view(), name="pick-update"),
    path("inventory/pick/delete/<int:pk>", views.PickAndPackDeleteView.as_view(), name="pick-delete"),
    path("inventory/pick/<int:pk>", views.PickAndPackDetailView.as_view(), name="pick-detail"),
    path("inventory/receive", views.ReceiveListView.as_view(), name="receive-list"),
    path("inventory/receive/create", views.ReceiveCreateView.as_view(), name="receive-create"),
    path("inventory/receive/<int:pk>", views.ReceiveDetailView.as_view(), name="receive-detail"),
    path("inventory/receive/update/<int:pk>", views.ReceiveUpdateView.as_view(), name="receive-update"),
    path("inventory/receive/delete/<int:pk>", views.ReceiveDeleteView.as_view(), name="receive-delete"),

]
