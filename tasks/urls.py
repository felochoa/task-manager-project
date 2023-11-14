from django.urls import path
from tasks.views import TaskPageView
from . import views


urlpatterns = [
path("tasks/", TaskPageView.as_view(), name="tasks"),
path('mark_completed/<int:task_id>/', views.mark_completed, name='mark_completed'),

]