from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fieds = '__all__'

    def validate(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            serializers.ValidationError("Publication can not exceed teh current year")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = 'BookSerializer'(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name']
