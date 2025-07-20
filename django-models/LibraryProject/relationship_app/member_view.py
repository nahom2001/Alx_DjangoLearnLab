# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library

# Role check function for Admin
def is_admin(user):
    # Ensure user is authenticated and has a UserProfile with role 'Admin'
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member, login_url='login')
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})

