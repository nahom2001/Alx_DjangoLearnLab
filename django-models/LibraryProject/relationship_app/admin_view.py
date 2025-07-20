# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library

# Role check function for Admin
def is_admin(user):
    # Ensure user is authenticated and has a UserProfile with role 'Admin'
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Admin view
@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

