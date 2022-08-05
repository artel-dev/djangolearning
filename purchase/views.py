from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

purchase_menu = [
    {"name": "", "title": "Purchase orders"},
]


def purchase_index(request):
    context = {
        "menu": purchase_menu,
    }
    return render(request, "purchase/purchase_index.html", context)



