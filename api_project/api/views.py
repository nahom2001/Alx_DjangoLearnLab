from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


## task 1 ##
#In api/views.py, create a view named BookList that extends rest_framework.generics.ListAPIView.
#Use the BookSerializer to serialize the data and the Book model as the queryset.

## task 2 ##
#In api/views.py, extend the existing view setup by adding a new class BookViewSet that handles all CRUD operations.
#Use rest_framework.viewsets.ModelViewSet, which provides implementations for various actions like list, create, retrieve, update, and destroy.