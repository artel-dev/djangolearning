from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import User, Partner


# Create your views here.


def index(request):
    return render(request, "references/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "references/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "references/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "references/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "references/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "references/register.html")


class UserListView(ListView):
    model = User
    template_name = "references/user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'user-create', 'title': 'create'},
        ]
        context["actions"] = actions
        return context


class UserCreateView(CreateView):
    model = User
    fields = [
        "name",
        "first_name",
        "last_name",
    ]
    template_name = "references/user_detail.html"
    success_url = reverse_lazy('user-list')


class UserUpdateView(UpdateView):
    model = User
    fields = [
        "name",
        "first_name",
        "last_name",
    ]
    template_name = "references/user_detail.html"
    success_url = reverse_lazy('user-list')


class UserDeleteView(DeleteView):
    model = User
    template_name = "references/user_confirm_delete.html"
    success_url = reverse_lazy('user-list')


class UserDetailView(DetailView):
    model = User
    template_name = "references/user_detail.html"
    success_url = reverse_lazy('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'user-update', 'title': 'edit'},
            {'name': 'user-delete', 'title': 'delete'},
        ]
        context["actions"] = actions
        return context


class PartnerListView(ListView):
    model = Partner
    template_name = "references/partner_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'partner-create', 'title': 'create'},
        ]
        context["actions"] = actions
        return context


class PartnerCreateView(CreateView):
    model = Partner
    fields = [
        "name",
        "description"
    ]
    template_name = "references/partner_detail.html"
    success_url = reverse_lazy('partner-list')


class PartnerUpdateView(UpdateView):
    model = Partner
    fields = [
        "name",
        "description"
    ]
    template_name = "references/partner_detail.html"
    success_url = reverse_lazy('partner-list')


class PartnerDeleteView(DeleteView):
    model = Partner
    template_name = "references/partner_confirm_delete.html"
    success_url = reverse_lazy('partner-list')


class PartnerDetailView(DetailView):
    model = Partner
    template_name = "references/partner_detail.html"
    success_url = reverse_lazy('partner-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'partner-update', 'title': 'edit'},
            {'name': 'partner-delete', 'title': 'delete'},
        ]
        context["actions"] = actions
        return context
