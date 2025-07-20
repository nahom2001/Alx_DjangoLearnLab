# relationship_app/views/admin_view.py
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator([login_required, role_required(['Member'])], name='dispatch')
class MemberView(View):
    def get(self, request):
        return render(request, 'relationship_app/member_view.html')
