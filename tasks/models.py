from django.db import models
from django.urls import reverse

class Task(models.Model):
    #task_id = models.AutoField(primary_key=True)
    author = models.ForeignKey("auth.User" ,on_delete=models.CASCADE, default="felipito")
    title = models.CharField(max_length=200)
    date = models.DateField()
    task_time = models.TimeField()
    details = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})