# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import TemplateView, CreateView
# from django.contrib import messages
# from django.urls import reverse_lazy
# from .models import Profile
# from django.contrib.auth.forms import UserCreationForm

# class UserLogIn(LoginView):
#     template_name = "account/login.html"
#     redirect_authenticated_user = True

#     def get_success_url(self):
#         return reverse_lazy('home')

# class UserLogoutView(LogoutView):
#     next_page = "/login.html/"

# class ProfileView(TemplateView):
#     template_name = "account/profile.html"