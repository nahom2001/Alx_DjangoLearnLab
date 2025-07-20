# django-models/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

def is_member(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
