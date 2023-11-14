from django.test import TestCase
from django.urls import reverse

from .models import Task

from datetime import datetime

#remember: only functions that start with the word test will be run when executing the tests.py
class TaskTest(TestCase):
    @classmethod
    # we can create a dummy database to make tests
    def setUpTestData(cls):
        cls.task = Task.objects.create(title = "test tittle", date = "2023-11-10", task_time = "11:00" , details = "testing details")

    def test_model_content(self):
        self.assertEqual(self.task.title, "test tittle")
        self.assertEqual(self.task.date, "2023-11-10")
        self.assertEqual(self.task.task_time, "11:00")
        self.assertEqual(self.task.details, "testing details")
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_name_is_correct(self):
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("tasks"))
        self.assertTemplateUsed(response, "tasks.html")
    
    def test_template_content_is_correct(self):
        response = self.client.get(reverse("tasks"))
        self.assertContains(response, "test tittle")
        self.assertContains(response, "2023-11-10")
        self.assertContains(response, "11:00")
        self.assertContains(response, "testing details")