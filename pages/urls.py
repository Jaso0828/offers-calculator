from django.urls import path
from . import views
from .views import HomePage
from .views import ContactUs
from .views import AboutUs, DashBoardPage


urlpatterns = [
    path('', HomePage.as_view(), name="index"),
    path('dasboard/', DashBoardPage.as_view(), name="dashboard"),
    path('contact/', ContactUs.as_view(), name="contact_us"),
    path('about/', AboutUs.as_view(), name="about_us")
    
]
