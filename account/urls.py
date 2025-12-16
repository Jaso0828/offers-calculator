from django.urls import path
from .views import UserLogIn, UserLogoutView, ProfileView

urlpatterns = [
    path("login/", UserLogIn.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile")
]
