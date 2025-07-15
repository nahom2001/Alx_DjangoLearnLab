from .models import Author, Book, Library, Librarian

def get_books_by_author(specific_author):
    books = Book.objects.filter(author=specific_author)
    return books

def get_books_in_library(specific_library):
    library = Library.objects.get(name=specific_library)
    books_in_library = Library.objects.all()
    return books_in_library

def get_librarian(specific_library):
    librarian = Library.objects.get(library__name=specific_library)    

    return librarian