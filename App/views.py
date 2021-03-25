from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView, redirect_to_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import *


class TaskListView(LoginRequiredMixin,ListView):

    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user) 
        context["count"] = context["tasks"].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)

        context['search_input']= search_input
        return context
    


class TaskDetailView(LoginRequiredMixin,DetailView):

    model = Task
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin,CreateView):
    template_name = 'App/task_create.html'
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('task_list')
    

    def form_valid(self, form) -> HttpResponse:
        form.instance.user = self.request.user
        return super(TaskCreateView,self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']

    success_url = reverse_lazy('task_list')
    template_name = "App/task_update.html"


class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task_list')
    template_name = "App/task_delete.html"
    
    


class UserLoginView(LoginView):
    
    fields = "__all__"
    template_name = "App/user_login.html"
    redirect_authenticated_user = True
    
    def get_success_url(self) -> object:
        return reverse_lazy('task_list')



class UserReigsterView(FormView):

    template_name = "App/user_register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task_list')

    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        if user is not None:
            login(self.request,user)

        return super(UserReigsterView,self).form_valid(form)
    



