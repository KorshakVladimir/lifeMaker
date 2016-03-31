import json
from datetime import datetime

from django.shortcuts import redirect
# from django.http import HttpResponse
from django.http import JsonResponse
# from django.views.generic import View
from django.views.generic import View
from django.views.generic import ListView

from . utils import exclude_token
from . models import Task
from . forms import TaskForm


class TaskCreate(View):
    def post(self, request):
        form = TaskForm(request.DATA)

        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse(form.errors, status=403)


class TaskList(ListView):
    model = Task
    template_name = 'tasks_manage/task_list.html'


class DeleteTasks(View):
    @exclude_token
    def post(self, request):
        Task.objects.filter(id__in = request.DATA).delete()
        return redirect('Task-list')


class CompleteTasks(View):
    @exclude_token
    def post(self, request):
        status_done = Task.get_done_status()
        date_now = datetime.now()
        Task.objects.filter(id__in = request.DATA).update(satus=status_done,
            date_execute=date_now)
        return redirect('Task-list')        


