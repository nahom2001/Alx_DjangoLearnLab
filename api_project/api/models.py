from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title} by {self.author}"


    #In api/models.py, define a Book model with basic fields such as title (a CharField) and author (a CharField).