from django.urls import path
from . import views

urlpatterns = [
    path('get_books/', views.get_books, name='get_books'),
]
