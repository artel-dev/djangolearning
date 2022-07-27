from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("user", views.UserListView.as_view(), name="user-list"),
    path("user/create", views.UserCreateView.as_view(), name="user-create"),
    path("user/update/<int:pk>", views.UserUpdateView.as_view(), name="user-update"),
    path("user/delete/<int:pk>", views.UserDeleteView.as_view(), name="user-delete"),
    path("user/<int:pk>", views.UserDetailView.as_view(), name="user-detail"),
]
