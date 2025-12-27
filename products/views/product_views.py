from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from products.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    fields='__all__'

    context_object_name = 'product_create'
    success_url = reverse_lazy('products:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'

    template_name_suffix = '_update_form'
    success_url = reverse_lazy('products:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')
    