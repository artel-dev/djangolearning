from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import SaleInvoice
from .forms import sale_invoice_formset


sale_menu = [
    {"name": "", "title": "Sale orders"},
    {"name": "sale-invoice-list", "title": "Sale invoices"},
]


def sale_index(request):
    context = {
        "menu": sale_menu,
    }
    return render(request, "sale/sale_index.html", context)


class SaleInvoiceListView(ListView):
    model = SaleInvoice
    template_name = "sale/sale_invoice_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'sale-invoice-create', 'title': 'create'},
        ]
        context["menu"] = sale_menu
        context["actions"] = actions
        return context


class SaleInvoiceCreateView(CreateView):
    model = SaleInvoice
    # fields = [
    #     "date",
    #     "number",
    # ]
    fields = '__all__'
    template_name = "sale/sale_invoice_detail.html"
    success_url = reverse_lazy('sale-invoice-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # actions = [
        #     {'name': 'product-update', 'title': 'edit'},
        #     {'name': 'product-delete', 'title': 'delete'},
        # ]
        # context["actions"] = actions
        context["menu"] = sale_menu
        if self.request.POST:
            context["sale_invoice_formset"] = sale_invoice_formset(self.request.POST)
        else:
            context["sale_invoice_formset"] = sale_invoice_formset(queryset=SaleInvoice.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = sale_invoice_formset(request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.render_to_response(self.get_context_data())

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()

        # with transaction.atomic():
        #     instance = form.save()
        #     formset.instance = instance
        #     formset.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class SaleInvoiceUpdateView(UpdateView):
    model = SaleInvoice
    fields = '__all__'
    template_name = "sale/sale_invoice_detail.html"
    success_url = reverse_lazy('sale-invoice-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # actions = [
        #     {'name': 'product-update', 'title': 'edit'},
        #     {'name': 'product-delete', 'title': 'delete'},
        # ]
        # context["actions"] = actions
        context["menu"] = sale_menu
        if self.request.POST:
            context["sale_invoice_formset"] = sale_invoice_formset(self.request.POST, instance=self.get_object())
        else:
            context["sale_invoice_formset"] = sale_invoice_formset(instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = sale_invoice_formset(request.POST, instance=self.get_object())
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
            # formset.save()
            # return render(request, "sale/sale_index.html")
        else:
            return self.render_to_response(self.get_context_data())

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()

        # with transaction.atomic():
        #     instance = form.save()
        #     formset.instance = instance
        #     formset.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class SaleInvoiceDeleteView(DeleteView):
    model = SaleInvoice
    template_name = "sale/sale_invoice_confirm_delete.html"
    success_url = reverse_lazy('sale-invoice-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = sale_menu
        return context


class SaleInvoiceDetailView(DetailView):
    model = SaleInvoice
    template_name = "sale/sale_invoice_detail.html"
    success_url = reverse_lazy('sale-invoice-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'sale-invoice-update', 'title': 'edit'},
            {'name': 'sale-invoice-delete', 'title': 'delete'},
        ]
        context["menu"] = sale_menu
        context["actions"] = actions
        return context
