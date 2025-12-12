from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'pages/index.html'



# About us
class AboutUs(TemplateView):
    template_name = 'pages/about_us.html'


# Contact us
class ContactUs(TemplateView):
    template_name = 'pages/contact_us.html'




# def index(request):
#     return render(request, 'pages/index.html')