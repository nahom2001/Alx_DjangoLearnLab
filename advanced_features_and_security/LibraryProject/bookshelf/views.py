from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book  # Assuming you have a Book model

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Fetch all books from the database
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})