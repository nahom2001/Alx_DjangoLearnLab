# admin_view.py
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View
from django.shortcuts import render

class AdminView(UserPassesTestMixin, View):
    def test_func(self):
        return getattr(self.request.user, 'userprofile', None) and self.request.user.userprofile.role == 'Admin'

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_dashboard.html')

# Don't forget to include this in your urls.py