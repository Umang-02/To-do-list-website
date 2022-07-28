from asyncio import tasks
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name="tasks_list"
    template_name="../templates/task_list.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks_list']=context['tasks_list'].filter(user=self.request.user)
        return context
class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    template_name="../templates/task_detail.html"
    context_object_name='task'
class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    template_name="../templates/create_task.html"
    fields='__all__'
    success_url=reverse_lazy('tasks')
    def form_invalid(self,form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)
class UpdateTask(LoginRequiredMixin,UpdateView):
    model=Task
    template_name="../templates/update_task.html"
    fields='__all__'
    success_url=reverse_lazy('tasks')
class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    template_name="../templates/task_delete.html"
    context_object_name='task'
    success_url=reverse_lazy('tasks')
class Login(LoginView):
    template_name="../templates/home.html"
    fields="__all__"
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('tasks')
def homepage(request):
    return render(request,'home.html')
class Register(FormView):
    template_name="../templates/register.html"
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy("tasks")
    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(Register,self).form_valid(form)