from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['book', 'member', 'issued_by', 'status', 'due_on']
    list_filter = ['status', 'issued_on']
    search_fields = ['book__title', 'member__username']
