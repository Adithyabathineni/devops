from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm  # make sure forms.py exists with RegisterForm

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
