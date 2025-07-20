from django.utils.decorators import method_decorator
from django.views import View

def is_admin(user):
    print("DEBUG: User:", user.username, "Role:", getattr(user, 'profile', None) and user.profile.role)
    return user.is_authenticated and hasattr(user, "profile") and user.profile.role == 'Admin'

@method_decorator(user_passes_test(is_admin, login_url='/login/'), name='dispatch')
class AdminView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'admin_view.html')

