from django.db import models

# Define the Author model to represent authors
class Author(models.Model):
    name = models.CharField(max_length=200)

    # magic method to have the string representation of the name field
    def __str__(self):
        return self.name


# Define the Book model to represent books
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    
    # Foreign key field used to represent 'one-to-many' relationship between the author and books.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    # magic method to have the string representation of the title field
    def __str__(self):
        return self.title
