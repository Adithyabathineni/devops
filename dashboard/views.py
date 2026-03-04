from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from accounts.models import User  # ← FIXED: Import from accounts, not dashboard
from catalog.models import Book, Category
from circulation.models import Loan


def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Login required")
            if request.user.role not in allowed_roles:
                return HttpResponseForbidden("Access denied")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

@login_required
@role_required(['user'])
def user_dashboard(request):
    active_loans = Loan.objects.filter(member=request.user, status__in=['active', 'requested']).select_related('book')
    context = {
        'page_title': 'My Dashboard',
        'active_loans': active_loans,
        'total_loans': active_loans.count(),
    }
    return render(request, 'dashboard/user.html', context)

@login_required
@role_required(['staff', 'admin'])
def staff_dashboard(request):
    overdue_loans = Loan.objects.filter(status='overdue')[:10]
    total_books = Book.objects.count()
    total_categories = Category.objects.count()
    context = {
        'page_title': 'Staff Dashboard',
        'overdue_loans': overdue_loans,
        'total_books': total_books,
        'total_categories': total_categories,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
@role_required(['admin'])
def admin_dashboard(request):
    total_users = User.objects.count()
    total_books = Book.objects.count()
    active_loans = Loan.objects.filter(status='active').count()
    overdue_loans = Loan.objects.filter(status='overdue').count()
    
    context = {
        'page_title': 'Admin Dashboard',
        'total_users': total_users,
        'total_books': total_books,
        'active_loans': active_loans,
        'overdue_loans': overdue_loans,
    }
    return render(request, 'dashboard/admin.html', context)
