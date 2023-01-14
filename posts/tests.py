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


class PostDetailViewTests(APITestCase):
    def setUp(self):
        tom = User.objects.create_user(username='tom', password='test')
        george = User.objects.create_user(username='george', password='test')
        Post.objects.create(
            owner=tom, plant='a plant', question='toms plant'
        )
        Post.objects.create(
            owner=george, plant='a cactus', question='georges plant'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['plant'], 'a plant')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_not_fetch_post_with_invalid_id(self):
        response = self.client.get('/posts/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_edit_own_post(self):
        self.client.login(username='tom', password='test')
        response = self.client.put('/posts/1/', {'plant': 'new plant'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.plant, 'new plant')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_not_edit_another_users_post(self):
        self.client.login(username='george', password='test')
        response = self.client.put('/posts/1/', {'plant': 'new plant'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
