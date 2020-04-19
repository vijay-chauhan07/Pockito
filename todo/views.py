from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import(TodoCreateForm, 
TodoUpdateForm,
RegistrationForm,
ProfileUpdateForm)
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages
#from .tasks import create_random_user_accounts
#from django.contrib import messages
#from django.views.generic.edit import FormView


# Create your views here.


class Home(TemplateView):
    template_name = 'base.html'


class SignUpView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration/signUp.html'
    success_url = reverse_lazy('login')
    success_message = "Congratulation '%(username)s',  Your Account Has Been Created  Sucessfully."


class TodoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Todo
    form_class = TodoCreateForm
    template_name = r'todo/todo_create_form.html'

    login_url = 'login'
    success_message = "'%(title)s'  has been created successfully."

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TodoListView(LoginRequiredMixin, ListView):
    paginate_by = 2
    model = Todo
    template_name = 'todo/list.html'
    context_object_name = "latest_reminder"

    def get_queryset(self):
        if self.request.user.is_authenticated:

            return Todo.objects.filter(author=self.request.user).order_by('-updated')
        else:
            pass


class TodoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Todo
    template_name = 'todo/detail.html'
    login_url = 'login'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user




class TodoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Todo
    #fields = ('title', 'description', 'deadline')
    form_class = TodoUpdateForm
    template_name = "todo/todo_update_form.html"
    success_message = "You are updated sucessfully."

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class DeleteTodoView(SuccessMessageMixin, DeleteView):
    model = Todo
    template_name = "todo/delete_todo_post.html"
    success_url = reverse_lazy('list')
    success_message = '%(title)s has been deleted sucessfully.'


class ProfileView( LoginRequiredMixin, UserPassesTestMixin ,DetailView):


        model = User
        template_name = "todo/profile.html"
        context_object_name = 'profile'
    
    
    
        def test_func(self):
            obj = self.get_object()
            print(self)
            return obj.id == self.request.user.id

    
class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    #fields = ('title', 'description', 'deadline')
    form_class = ProfileUpdateForm
    template_name = "todo/profile_update_form.html"

    success_message = "You are Profile  updated sucessfully."


    def test_func(self):
        obj = self.get_object()
        return obj.id == self.request.user.id




    def get_success_url(self, *args, **kwargs):

        return reverse_lazy('profile', args=[self.request.user.pk])

    
