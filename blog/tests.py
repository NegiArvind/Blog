
from .models import Post
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
# Create your tests here.
class BlogTests(TestCase):

    def setup(self):
        self.user=get_user_model().objects.create_user(username='admin',email='admin@gmail.com',password='admin')
        self.post=Post.objects.create(title='A good title',body='Nice body content',author=self.user,)

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'admin')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200) # code 200 means site is working fine
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/3/')
        no_response = self.client.get('/post/10000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404) # used to check whther both two are equal or not
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
