from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Task

# Create your views here.
class TaskPageView(ListView):
    model = Task
    template_name = "tasks.html"

def mark_completed(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        task.is_completed = not task.is_completed  # Invierte el estado de completado
        task.save()
    
    return redirect('tasks')