from django.shortcuts import render

# Create your views here.
from .models import Book  # Assuming you have a Book model

def book_list(request):
    # Fetch all books from the database
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})