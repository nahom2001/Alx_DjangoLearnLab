from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def is_admin(user):
    if hasattr(user, 'userprofile'):
        return user.userprofile.role == 'Admin'
    logger.warning("UserProfile does not exist for user: %s", user.username)
    return False

@user_passes_test(is_admin)
def admin_view(request):
    # Logic for the admin view
    return render(request, 'admin_dashboard.html')