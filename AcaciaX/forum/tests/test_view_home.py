from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import home, category_topics
from ..models import Category

from ..forms import NewTopicForm

class ForumTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Django', description='Django board.')
        url = reverse('forum')
        self.response = self.client.get(url)

    def test_forum_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)
