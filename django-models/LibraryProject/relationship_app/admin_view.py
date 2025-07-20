# django-models/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

def is_admin(user):
    if not user.is_authenticated:
        return False
    try:
        return user.profile.role == 'Admin'
    except AttributeError:
        return False
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Admin'


@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'admin_view.html')

