from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)

    books = Library.objects.all()
    return books.all()

def get_librarian(specific_library):
    library = Library.objects.get(library__name=specific_library)    
       librarian = Librarian.objects.get(library=library)

    return librarian