from django.urls import path
from . import views
from .views import HomePage
from .views import ContactUs
from .views import AboutUs


urlpatterns = [
    path('', HomePage.as_view(), name="index"),
    path('contact_us/', ContactUs.as_view(), name="contact_us"),
    path('about_us/', AboutUs.as_view(), name="about_us")
    
]
