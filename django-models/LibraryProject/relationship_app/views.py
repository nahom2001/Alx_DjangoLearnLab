from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def get_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, 'relationship_app/list_books.html', context )
