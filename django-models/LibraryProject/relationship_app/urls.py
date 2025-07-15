from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    path('get_books/', views.get_books, name='get_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail')
]
