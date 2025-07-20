# django-models/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')
