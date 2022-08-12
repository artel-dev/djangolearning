from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PurchaseOrder
from .forms import purchase_order_formset, PurchaseOrderForm

purchase_menu = [
    {"name": "purchase-orders", "title": "Purchase orders"},
]


def purchase_index(request):
    context = {
        "menu": purchase_menu,
    }
    return render(request, "purchase/purchase_index.html", context)


class PurchaseOrderListView(ListView):
    model = PurchaseOrder
    template_name = 'purchase/purchase_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'purchase-orders-create', 'title': 'create'},
        ]
        context["actions"] = actions
        context["menu"] = purchase_menu
        return context


class PurchaseOrderCreate(CreateView):
    model = PurchaseOrder
    # fields = [
    #     "date",
    #     "number",
    # ]
    fields = '__all__'
    template_name = "purchase/purchase_order_detail.html"
    # success_url = reverse_lazy('purchase_list')


def purchase_order_create(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')

    else:
        form = PurchaseOrderForm()
    return render(request, 'purchase/purchase_index.html', {'form': form, 'menu': purchase_menu})

