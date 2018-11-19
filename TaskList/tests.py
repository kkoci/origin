"""
These are just 4 simple tests for our application
"""
from django.test import TestCase, SimpleTestCase
from django.core.urlresolvers import reverse
from TaskList.models import Task

class HomePageTests(SimpleTestCase):
    """
    Just 3 simple tests about http responses
    """
    def test_home_page_status_code(self):
        """
        Check if the login page is working properly
        """
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        """
        Check if the url actually exists
        """
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Check if the right url associated template is loading
        """
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'layout.html')

class TaskTests(TestCase):
    """
    Our minimalistic model test :)
    """
    def setUp(self):
        """
        The setup for our model test
        """
        self.task = Task(name="Test1",
                         description="Alors",
                         start="2018-12-11 12:12",
                         end="2018-12-12 12:45",
                         user_id=1
                        )

    def test_task_name(self):
        """
        Check if the task is created properly
        """
        self.assertEqual(self.task.name, 'Test1')
