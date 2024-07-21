from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import Post, Comment

User = get_user_model()

class BlogTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpass123',
            role='author'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user
        )

    def test_blog_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_blog_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_blog_create_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('post_create'), {
            'title': 'New Test Post',
            'content': 'New test content',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New Test Post')

    def test_blog_update_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('post_edit', args=[self.post.id]), {
            'title': 'Updated Test Post',
            'content': 'Updated test content',
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Test Post')

    def test_blog_delete_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('post_delete', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)

    def test_api_post_list(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_api_post_detail(self):
        response = self.client.get(f'/api/posts/{self.post.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Post')

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'role': 'reader'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_role_based_access(self):
        reader = User.objects.create_user(
            username='reader', 
            email='reader@example.com', 
            password='testpass123',
            role='reader'
        )
        self.client.login(username='reader', password='testpass123')
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 403)  # Forbidden for readers