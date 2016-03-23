# from django.http import HttpResponse
# from django.views.generic import View

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from . models import Task


class TaskCreate(CreateView):
    model = Task
    fields = ['title']


class TaskUpdate(UpdateView):
    model = Task
    fields = ['name']


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('author-list')


class TaskList(ListView):
    model = Task
    template_name = 'tasks_manage/task_list.html'



