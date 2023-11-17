
from django.urls import path
from tasks.views import TaskPageView, TaskCompletedView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from . import views

urlpatterns = [
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/new/', TaskCreateView.as_view(), name='create_task'),
    
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path("tasks/", TaskPageView.as_view(), name="tasks"),
    path("completed_tasks/", TaskCompletedView.as_view(), name="completed_tasks"),  
    path('tasks/<int:pk>/mark_completed/', views.mark_completed, name='mark_completed'),
    path('tasks/<int:pk>/mark_uncompleted/', views.mark_uncompleted, name='mark_uncompleted'),
]


