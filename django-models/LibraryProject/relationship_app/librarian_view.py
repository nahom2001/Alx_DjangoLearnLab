# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library

# Role check function for Admin
def is_admin(user):
    # Ensure user is authenticated and has a UserProfile with role 'Admin'
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Admin view
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome transparent='login'})

