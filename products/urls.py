from django.urls import path

from .views import (IngredientDetailView, IngredientListView, ProductMenu)

urlpatterns = [
    path('ingredients/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredients/<int:pk>/', IngredientDetailView.as_view(), name='ingredient_details'),
    path('', ProductMenu.as_view(), name='products')
]
