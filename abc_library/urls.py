"""
URL configuration for abc_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from circulation import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('catalog.urls')),
    path('circulation/', include('circulation.urls')),
    path('dashboard/', include('dashboard.urls')),
    path("request/<int:book_id>/", views.request_loan, name="request_loan"),
    path("approve/<int:loan_id>/", views.approve_loan, name="approve_loan"),
    path("return/<int:loan_id>/", views.mark_returned, name="mark_returned"),
]
