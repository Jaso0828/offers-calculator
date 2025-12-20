from django.urls import path

from .views import (IngredientDetailView, IngredientListView, ProductMenu, IngredietCreateView, IngredientUpdateView, IngredientDeleteView)

urlpatterns = [
    path('ingredients/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient_details'),
    path('ingredients/create', IngredietCreateView.as_view(), name='ingredient_create'),
    path('ingredients/update/<int:pk>', IngredientUpdateView.as_view(), name='ingredient_update'),
    path('ingredients/delete/<int:pk>', IngredientDeleteView.as_view(), name='ingredient_delete'),
    path('', ProductMenu.as_view(), name='products')
]
