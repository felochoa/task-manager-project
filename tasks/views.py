from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Task

# Create your views here.
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    #we use reverse_lazy here as opposed to just reverse so that it won’t execute
    #the URL redirect until our view has finished deleting the task.
    success_url = reverse_lazy("tasks")

class TaskCreateView(CreateView):  
    model = Task
    template_name = "new_task.html"
    fields = ["title", "author", "date", "task_time", "details"]

class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task_edit.html"
    fields = ["title", "date", "task_time", "details"]
    
 


class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = 'task'


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
         
def mark_completed(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()

    if task.is_completed:
        return redirect('completed_tasks')
    else:
        return redirect('tasks')

def mark_uncompleted(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()

    return redirect('completed_tasks' if task.is_completed else 'tasks')