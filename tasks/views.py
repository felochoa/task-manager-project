from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Task

# Create your views here.
class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'

class TaskPageView(ListView):
    model = Task
    template_name = "tasks.html"
    context_object_name = 'task_list'

    def get_queryset(self): 
        return Task.objects.filter(is_completed = False)

class TaskCompletedView(ListView):
    model = Task
    template_name = "completed_tasks.html"
    context_object_name = "completed_tasks"
    

    def get_queryset(self):
        return Task.objects.filter(is_completed = True)
         

def mark_completed(request, task_id):
        
        task = Task.objects.get(pk=task_id)

        if request.method == 'POST':
            task.is_completed = not task.is_completed  # Invierte el estado de completado
            task.save()

        task.completed = task.is_completed
        task.save()

        if task.is_completed:
            return redirect('completed_tasks')
        else:
            return redirect('tasks')

def mark_uncompleted(request, task_id):
     
     task = Task.objects.get(pk=task_id)

     if request.method == 'POST':
            task.is_completed = not task.is_completed  # Invierte el estado de completado
            task.save()
    
     return redirect('completed_tasks' if task.is_completed else 'tasks')