from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

#In api/views.py, create a view named BookList that extends rest_framework.generics.ListAPIView.
#Use the BookSerializer to serialize the data and the Book model as the queryset.