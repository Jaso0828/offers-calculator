from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Ingredient

# Create your views here.
class ProductMenu(TemplateView):
    template_name = 'products/products.html'


class IngredientListView(ListView):
    model = Ingredient
    context_object_name = 'ingredients'


class IngredientDetailView(DetailView):
    model = Ingredient
    context_object_name = 'ingredient'


class IngredietCreateView(CreateView):
    model = Ingredient
    fields='__all__'

    context_object_name = 'ingredient_create'
    success_url = reverse_lazy('products:ingredient_list')


class IngredientUpdateView(UpdateView):
    model = Ingredient
    fields = '__all__'

    template_name_suffix = '_update_form'
    success_url = reverse_lazy('products:ingredient_list')


class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('products:ingredient_list')
    