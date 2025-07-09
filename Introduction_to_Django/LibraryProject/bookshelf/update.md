from bookshelf.models import Book

book1 = Book.objects.get(publication_date=1984)
book1.title = "Nineteen Eighty Four" 
