from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.RoleBasedLoginView.as_view(), name="login"),
    path("login/redirect/", views.login_redirect, name="login_redirect"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
