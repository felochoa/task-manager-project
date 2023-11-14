from django.db import models

# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    task_time = models.TimeField()
    details = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title