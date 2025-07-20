from django.utils.decorators import method_decorator
from django.views import View

def is_admin(user):
    return user.is_authenticated and hasattr(user, "profile") and user.profile.role == 'Admin'

@method_decorator(user_passes_test(is_admin, login_url='/login/'), name='dispatch')
class AdminView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'admin_view.html')
