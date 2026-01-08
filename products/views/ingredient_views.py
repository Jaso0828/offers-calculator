from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from ..models import Ingredient
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProductMenu(TemplateView):
    template_name = 'products/products.html'


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    context_object_name = 'ingredients'


class IngredientDetailView(LoginRequiredMixin ,DetailView):
    model = Ingredient
    context_object_name = 'ingredient'


class IngredientCreateView(LoginRequiredMixin ,CreateView):
    model = Ingredient
    fields='__all__'

    context_object_name = 'ingredient_create'
    success_url = reverse_lazy('products:ingredient_list')


class IngredientUpdateView(LoginRequiredMixin,UpdateView):
    model = Ingredient
    fields = '__all__'

    template_name_suffix = '_update_form'
    success_url = reverse_lazy('products:ingredient_list')


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = reverse_lazy('products:ingredient_list')
    