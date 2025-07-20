from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def check_role(role):
    def role_check(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return role_check

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html')
