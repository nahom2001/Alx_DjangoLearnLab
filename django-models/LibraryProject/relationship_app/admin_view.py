# django-models/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

def is_admin(user):
    print("DEBUG Role:", getattr(user, "profile", None) and user.profile.role)
    return user.is_authenticated and hasattr(user, "profile") and user.profile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    print("DEBUG: Admin view accessed by", request.user)
    return render(request, 'admin_view.html')
