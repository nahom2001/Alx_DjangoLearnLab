from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('profile')  

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'  

# Profile Management View
@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    form_class = UserProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user  # Return the current user

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return self.post(request, *args, **kwargs)  # Handle POST requests
        return super().dispatch(request, *args, **kwargs)  # Handle GET requests

    def form_valid(self, form):
        form.save()  # Save the updated user information
        return super().form_valid(form)  # Redirect to success_url

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))