from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import role_required

@method_decorator([login_required, role_required(['Admin'])], name='dispatch')
class AdminView(View):
    def get(self, request):
        return render(request, 'relationship_app/admin_view.html')
