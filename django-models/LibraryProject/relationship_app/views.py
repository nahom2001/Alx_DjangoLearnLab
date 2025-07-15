from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def get_books(request):
    books = Book.objects.all()
    return books
