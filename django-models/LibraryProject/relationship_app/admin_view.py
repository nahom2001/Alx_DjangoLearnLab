from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

#Test function for role-based access
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


@user_passses_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')