from django.urls import path
from . import views

urlpatterns = [
    path("inventory", views.inventory_index, name="inventory-index"),
    path("inventory/pick", views.PickAndPackListView.as_view(), name="pick-list"),
    path("inventory/pick/create", views.PickAndPackCreateView.as_view(), name="pick-create"),
    path("inventory/pick/update/<int:pk>", views.PickAndPackUpdateView.as_view(), name="pick-update"),
    path("inventory/pick/delete/<int:pk>", views.PickAndPackDeleteView.as_view(), name="pick-delete"),
    path("inventory/pick/<int:pk>", views.PickAndPackDetailView.as_view(), name="pick-detail"),
]
