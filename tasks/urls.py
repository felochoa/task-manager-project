
from django.urls import path
from tasks.views import TaskPageView, TaskCompletedView, TaskDetailView
from . import views

urlpatterns = [
    path('tasks/<int:task_id>/', TaskDetailView.as_view(), name='task_detail'),
    path("tasks/", TaskPageView.as_view(), name="tasks"),
    path("completed_tasks/", TaskCompletedView.as_view(), name="completed_tasks"), 
    path('tasks/<int:task_id>/mark_completed/', views.mark_completed, name='mark_completed'),
    path('tasks/<int:task_id>/mark_uncompleted/', views.mark_uncompleted, name='mark_uncompleted'),
]