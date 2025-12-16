from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from .models import Ingredient

# Create your views here.
class ProductMenu(TemplateView):
    template_name = 'products/products.html'


class IngredientListView(ListView):
    model = Ingredient
    context_object_name = 'ingredient_list'


class IngredientDetailView(DetailView):
    model = Ingredient