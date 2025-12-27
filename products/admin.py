from django.contrib import admin
from products.models import Product, Ingredient

# Register your models here.
admin.site.register([Product])
admin.site.register([Ingredient])