from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm  # make sure forms.py exists with RegisterForm
from django.contrib.auth.views import LoginView
from django.urls import reverse

class RoleBasedLoginView(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        # after successful login, send to our login_redirect view
        return reverse("accounts:login_redirect")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your ABC Library account was created successfully.")
            return redirect("catalog:home")
        else:
            messages.error(request, "There was a problem with your registration. Please fix the errors below.")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "accounts/profile.html")


def logout_view(request):
    logout(request)
    return redirect("catalog:home")

def login_redirect(request):
    user = request.user
    if user.role == user.ROLE_ADMIN:
        return redirect("dashboard:admin")
    elif user.role == user.ROLE_STAFF:
        return redirect("dashboard:staff")
    else:
        return redirect("dashboard:user")