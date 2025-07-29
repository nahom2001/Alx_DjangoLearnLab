from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)),

]



# In api/urls.py, import DefaultRouter from rest_framework.routers and register your BookViewSet.
# Register the BookViewSet with the router as follows:
# router.register(r'books_all', BookViewSet, basename='book_all')