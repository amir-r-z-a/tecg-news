from django.test import TestCase
from rest_framework.utils import json

from .models import News, Tag


# Create your tests here.

class NewsTestCase(TestCase):
    def setUp(self):
        News.objects.create(title="Apple new mack", text="here is apples new mack")
        News.objects.create(title="samsung new phone", text="here is samsung new phone")
        News.objects.create(title="xiaomi new phone", text="here is xiaomi new phone")

        Tag.objects.create(name="tech")
        Tag.objects.create(name="phone")

        news1 = News.objects.get(title="Apple new mack")
        news2 = News.objects.get(title="samsung new phone")
        news3 = News.objects.get(title="xiaomi new phone")

        tag1 = Tag.objects.get(name="tech")
        tag2 = Tag.objects.get(name="phone")

        tag1.news.add(news1, news3, news2)

        tag2.news.add(news3, news2)

    def test_tag1(self):
        tech_tags = Tag.objects.get(name="tech")
        tech_news = tech_tags.news.all()
        self.assertEquals(len(tech_news), 3)

    def test_tag2(self):
        phone_tags = Tag.objects.get(name="phone")
        phone_news = phone_tags.news.all()
        self.assertEquals(len(phone_news), 2)

    def test_get_news_list(self):
        with self.captureOnCommitCallbacks(execute=True):
            response = self.client.get(path="/news/")
        get_news = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(get_news), 3)

    # def test_post_news_list(self):
    #     with self.captureOnCommitCallbacks(execute=True) as callbacks:
    #         response = self.client.post(path="/news/", data={"title": "mahshad"})
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(callbacks), 1)
