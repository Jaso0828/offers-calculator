from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

class UserLogIn(LoginView):
    template_name = "account/login.html"

class UserLogoutView(LogoutView):
    next_page = "/login.html/"

class ProfileView(TemplateView):
    template_name = "account/profile.html"