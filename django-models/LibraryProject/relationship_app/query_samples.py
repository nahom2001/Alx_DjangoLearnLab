from .models import Author, Book, Library, Librarian

def get_books_by_author(specific_author):
    books = Book.objects.filter(author=specific_author)
    return books

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)

    books = Library.objects.all()
    return books.all()

def get_librarian(specific_library):
    librarian = Library.objects.get(library__name=specific_library)    

    return librarian