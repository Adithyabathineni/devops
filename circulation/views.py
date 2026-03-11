from datetime import date, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect

from catalog.models import Book
from .models import Loan


@login_required
def request_loan(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.copies_available < 1:
        messages.error(request, "No available copies for this book right now.")
        return redirect("catalog:home")

    exists = Loan.objects.filter(
        book=book,
        member=request.user,
        status__in=["requested", "active"],
    ).exists()
    if exists:
        messages.warning(request, "You already have a pending or active loan for this book.")
        return redirect("catalog:home")

    Loan.objects.create(
        book=book,
        member=request.user,
        issued_by=request.user,  # simple for now
        issued_on=date.today(),
        due_on=date.today() + timedelta(days=14),
        status="requested",
    )
    messages.success(request, "Borrow request created. Library staff will review it.")
    return redirect("dashboard:user")


@login_required
def approve_loan(request, loan_id):
    if not request.user.is_library_staff:
        return HttpResponseForbidden("Staff only")
    loan = get_object_or_404(Loan, pk=loan_id, status="requested")
    loan.status = "active"
    loan.issued_by = request.user
    loan.save()
    loan.book.copies_available -= 1
    loan.book.save()
    messages.success(request, "Loan approved.")
    return redirect("dashboard:staff")


@login_required
def mark_returned(request, loan_id):
    if not request.user.is_library_staff:
        return HttpResponseForbidden("Staff only")
    loan = get_object_or_404(Loan, pk=loan_id, status__in=["active", "overdue"])
    loan.status = "returned"
    loan.returned_on = date.today()
    loan.save()
    loan.book.copies_available += 1
    loan.book.save()
    messages.success(request, "Book marked as returned.")
    return redirect("dashboard:staff")
