from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTest(APITestCase):
    """
    Define set up method and create a user that can be used in the tests
    """
    def setUp(self):
        User.objects.create_user(username='tom', password='test')

    def test_can_list_posts(self):
        tom = User.objects.get(username='tom')
        Post.objects.create(owner=tom, plant='a plant')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='tom', password='test')
        response = self.client.post('/posts/', {'plant': 'a plant'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_can_not_create_post(self):
        response = self.client.post('/posts/', {'plant': 'a plant'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)