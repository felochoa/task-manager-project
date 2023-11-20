from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Task

from datetime import datetime

#remember: only functions that start with the word test will be run when executing the tests.py
class TaskTest(TestCase):
    @classmethod
    # created a dummy database to make tests
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username = "felipito", email="test@email.com" , password ="secret")
        cls.task = Task.objects.create(title = "test tittle", author = cls.user, date = "2023-11-10", task_time = "11:00" , details = "testing details")
        cls.task_completed = Task.objects.create(title = "complete tittle", author = cls.user, date = "2023-11-10", task_time = "11:00" , details = "testing details", is_completed=True)

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
        #self.assertContains(response, "2023-11-10")
        #self.assertContains(response, "11:00")
        self.assertContains(response, "testing details")
    
    def test_url_exists_at_correct_location_completed_tasks(self):
            response = self.client.get("/completed_tasks/")
            self.assertEqual(response.status_code, 200)

    def test_template_content_is_correct_completed_tasks(self):
        response = self.client.get(reverse("completed_tasks"))
        self.assertContains(response, self.task_completed.title)      
        self.assertContains(response, self.task_completed.details)
    
    def test_url_name_is_correct_completed_tasks(self):
        response = self.client.get(reverse("completed_tasks"))
        self.assertEqual(response.status_code, 200)
    
    def test_post_detailview(self):
        response = self.client.get(reverse("task_detail",kwargs={"pk": self.task.id}))
        self.assertEqual(response.status_code, 200)
        no_response = self.client.get("/post/100000/")
        self.assertEqual(no_response.status_code, 404)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/tasks/1/")
        self.assertEqual(response.status_code, 200)
    
    ####################################################################################
    #tests for create, delete, edit views

    def test_task_create_view(self):
        response = self.client.post(reverse("create_task"), {"title": "new task","date":"2023-11-16", "author":self.user.id, "task_time": "11:00", "details": "new task"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.last().title, "new task")
        #self.assertEqual(Task.objects.last().date, "2023-11-16")
        #self.assertEqual(Task.objects.last().task_time, "11:00")
        self.assertEqual(Task.objects.last().details, "new task")

    def test_task_edit_view(self):
        response = self.client.post(reverse("task_edit", kwargs={'pk': Task.objects.last().pk}), {"title": "updated task", "date":"2023-11-16", "task_time": "11:00", "details": "updated detail of task",},)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.last().title, "updated task")
        #self.assertEqual(Task.objects.last().date, "2023-11-16")
        #self.assertEqual(Task.objects.last().task_time, "11:00")
        self.assertEqual(Task.objects.last().details, "updated detail of task") 
    
    def test_task_delete_view(self):
        response = self.client.post(reverse("task_delete", kwargs={'pk': Task.objects.last().pk}))
        self.assertEqual(response.status_code, 302)