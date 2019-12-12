from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import home, category_topics
from ..models import Category

from ..forms import NewTopicForm


class ForumTopicsTests(TestCase):
    def setUp(self):
        Category.objects.create(name='Django', description='Django board.')

    def test_category_topics_view_success_status_code(self):
        url = reverse('category_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_category_topics_view_not_found_status_code(self):
        url = reverse('category_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_category_topics_url_resolves_category_topics_view(self):
        view = resolve('/forum/1/')
        self.assertEquals(view.func, category_topics)