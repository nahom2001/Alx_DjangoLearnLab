from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Post  # Assuming your blog post model is named Post
from .forms import CustomUserCreationForm, UserProfileForm

class ListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template to    of 
    context_object_name = 'posts'  

class DetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  
    context_object_name = 'post'  

@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'  
    fields = ['title', 'content']  
    success_url = reverse_lazy('post_list')  

@method_decorator(login_required, name='dispatch')
class UpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  
    fields = ['title', 'content']  # Fields to edit
    success_url = reverse_lazy('post_list')  # Redirect after successful update

    def get_queryset(self):
        # Ensure only the author can edit their post
        return Post.objects.filter(author=self.request.user)

# DeleteView to let authors delete their posts
@method_decorator(login_required, name='dispatch')
class DeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # Template for confirming deletion
    success_url = reverse_lazy('post_list')  # Redirect after successful deletion

    def get_queryset(self):
        # Ensure only the author can delete their post
        return Post.objects.filter(author=self.request.user)

# Registration and Authentication Views
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