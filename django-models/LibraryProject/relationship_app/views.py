from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
#Import generic classes for django generic view
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, 'relationship_app/list_books.html', context )



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Update with your template path
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Fetch all books related to the library
        return context


# class RegisterView(CreateView):
#     from_class = UserCreationForm
#     succcess_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         login(self.request, self.object)
#         return response


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')

        else:
            form = UserCreationForm()
        
        return render(request, 'relationship_app/register.html', {'form': form})