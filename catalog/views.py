from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book, Category

def home(request):
    featured_books = Book.objects.all().select_related('category')[:6]
    categories = Category.objects.all()
    context = {
        'featured_books': featured_books,
        'categories': categories,
        'total_books': Book.objects.count(),
    }
    return render(request, 'catalog/home.html', context)

def book_list(request):
    books = Book.objects.select_related('category').all()
    return render(request, 'catalog/book_list.html', {'books': books})
