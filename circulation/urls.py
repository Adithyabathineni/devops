from django.urls import path
from . import views

app_name = "circulation"

urlpatterns = [
    path("request/<int:book_id>/", views.request_loan, name="request_loan"),
]
