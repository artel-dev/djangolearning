from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import PickAndPack, Receive
from .forms import pick_and_pack_formset, receive_formset


inventory_menu = [
    {"name": "", "title": "Transfer"},
    {"name": "receive-list", "title": "Receive"},
    {"name": "", "title": "Putaway"},
    {"name": "pick-list", "title": "Pick and pack"},
]


def inventory_index(request):
    context = {
        "menu": inventory_menu,
    }
    return render(request, "inventory/inventory_index.html", context)

class ReceiveListView(ListView):
    model = Receive
    template_name = "inventory/receive_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'receive-create', 'title': 'create'},
        ]
        context["menu"] = inventory_menu
        context["actions"] = actions
        return context

class ReceiveCreateView(CreateView):
    model = Receive
    fields = '__all__'
    template_name = "inventory/receive_detail.html"
    success_url = reverse_lazy('receive-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = inventory_menu
        if self.request.POST:
            context["receive_formset"] = receive_formset(self.request.POST)
        else:
            context["receive_formset"] = receive_formset(queryset=Receive.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = receive_formset(request.POST)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.render_to_response(self.get_context_data())

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))

class ReceiveDetailView(DetailView):
    model = Receive
    template_name = "inventory/receive_detail.html"
    success_url = reverse_lazy('receive-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'receive-update', 'title': 'edit'},
            {'name': 'receive-delete', 'title': 'delete'},
        ]
        context["menu"] = inventory_menu
        context["actions"] = actions
        return context

class ReceiveUpdateView(UpdateView):
    model = Receive
    fields = '__all__'
    template_name = "inventory/receive_detail.html"
    success_url = reverse_lazy('receive-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = inventory_menu
        if self.request.POST:
            context["receive_formset"] = receive_formset(self.request.POST, instance=self.get_object())
        else:
            context["receive_formset"] = receive_formset(instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = receive_formset(request.POST, instance=self.get_object())
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.render_to_response(self.get_context_data())

    def form_valid(self, form, formset):
        self.object = form.save()
        formset.instance = self.object
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ReceiveDeleteView(DeleteView):
    model = Receive
    template_name = "inventory/receive_confirm_delete.html"
    success_url = reverse_lazy('receive-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = inventory_menu
        return context

class PickAndPackListView(ListView):
    model = PickAndPack
    template_name = "inventory/pick_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'pick-create', 'title': 'create'},
        ]
        context["menu"] = inventory_menu
        context["actions"] = actions
        return context


class PickAndPackCreateView(CreateView):
    model = PickAndPack
    # fields = [
    #     "date",
    #     "number",
    # ]
    fields = '__all__'
    template_name = "inventory/pick_detail.html"
    success_url = reverse_lazy('pick-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # actions = [
        #     {'name': 'product-update', 'title': 'edit'},
        #     {'name': 'product-delete', 'title': 'delete'},
        # ]
        # context["actions"] = actions
        context["menu"] = inventory_menu
        if self.request.POST:
            context["pick_and_pack_formset"] = pick_and_pack_formset(self.request.POST)
        else:
            context["pick_and_pack_formset"] = pick_and_pack_formset(queryset=PickAndPack.objects.none())
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = pick_and_pack_formset(request.POST)
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


class PickAndPackUpdateView(UpdateView):
    model = PickAndPack
    fields = '__all__'
    template_name = "inventory/pick_detail.html"
    success_url = reverse_lazy('pick-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # actions = [
        #     {'name': 'product-update', 'title': 'edit'},
        #     {'name': 'product-delete', 'title': 'delete'},
        # ]
        # context["actions"] = actions
        context["menu"] = inventory_menu
        if self.request.POST:
            context["pick_and_pack_formset"] = pick_and_pack_formset(self.request.POST, instance=self.get_object())
        else:
            context["pick_and_pack_formset"] = pick_and_pack_formset(instance=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = pick_and_pack_formset(request.POST, instance=self.get_object())
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


class PickAndPackDeleteView(DeleteView):
    model = PickAndPack
    template_name = "inventory/pick_confirm_delete.html"
    success_url = reverse_lazy('pick-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = inventory_menu
        return context


class PickAndPackDetailView(DetailView):
    model = PickAndPack
    template_name = "inventory/pick_detail.html"
    success_url = reverse_lazy('pick-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actions = [
            {'name': 'pick-update', 'title': 'edit'},
            {'name': 'pick-delete', 'title': 'delete'},
        ]
        context["menu"] = inventory_menu
        context["actions"] = actions
        return context
