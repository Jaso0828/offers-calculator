from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashBoardPage(LoginRequiredMixin, TemplateView):
    template_name = 'pages/dashboard.html'


class HomePage(TemplateView):
    template_name = 'pages/index.html'



# About us
class AboutUs(TemplateView):
    template_name = 'pages/about_us.html'


# Contact us
class ContactUs(TemplateView):
    template_name = 'pages/contact_us.html'



