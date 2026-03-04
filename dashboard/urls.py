from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('user/', views.user_dashboard, name='user'),
    path('staff/', views.staff_dashboard, name='staff'),
    path('admin/', views.admin_dashboard, name='admin'),
]
