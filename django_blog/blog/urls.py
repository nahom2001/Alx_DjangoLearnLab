from django.urls import path
from django.contrib.auth import views as  auth_views

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
