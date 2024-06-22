import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vanlife_blog.settings")
import django
django.setup()
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post, Journey

User= get_user_model()

class UserViewTests(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='testuser',password= 'something123',email= 'testuser@anything.com')
        self.client.login(username= 'testuser',password= 'something123')

    def test_register_view_post(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@anything.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())


    def test_login_view(self):
        response=self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_blog_feed_view(self):
        response= self.client.get(reverse('blog_feed'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_feed.html')

    def test_login_view_post(self):
        data = {
            'username': 'testuser',
            'password': 'something123'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)

    def test_profile_view(self):
        response= self.client.get(reverse('profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
    def test_profile_blogs_view(self):
        response= self.client.get(reverse('profile_blogs', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile_blogs.html')
    def test_logout_view(self):
        response=self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 302)



class BlogViewTests(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(username= 'testuser',password = 'password',email= 'testuser@anything.com')
        self.client.force_login(self.user)
        self.client.login(username= 'testuser',password= 'password')
        self.post = Post.objects.create(title= 'Test Post',content= 'Test Content',author=self.user)
        self.journey = Journey.objects.create(title='test journey', description='description of the journey', start_date='time and location', end_date='eternity', author=self.user)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html')
    def test_search_view(self):
        response= self.client.get(reverse('search'), {'q': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/search.html')

    def test_liked_blogs_view(self):
        response = self.client.get(reverse('liked_blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/liked_blogs.html')

    def test_post_like_view(self):
        response= self.client.post(reverse('post_like', args=[self.post.pk]))
        self.assertTrue(self.post.likes.filter(pk=self.user.pk).exists())
        self.assertEqual(response.status_code, 302)
    def test_post_unlike_view(self):
        self.post.likes.add(self.user)
        response = self.client.post(reverse('post_unlike', args=[self.post.pk]))
        self.assertFalse(self.post.likes.filter(pk=self.user.pk).exists())
        self.assertEqual(response.status_code, 302)

    def test_journey_create_view(self):
        response=self.client.get(reverse('journey_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/journey_edit.html')

    def test_join_journey(self):
        self.journey= Journey.objects.create(title= 'Test Journey',description ='Description of the journey',start_date= 'time and location', end_date='eternity', author=self.user)
        response=self.client.post(reverse('journey_join', args= [self.journey.id]))
        self.journey.refresh_from_db()
        self.assertIn(self.user, self.journey.participants.all())
        self.assertEqual(response.status_code, 302)


    def test_leave_journey(self):
        self.journey=Journey.objects.create(title= 'Test Journey', description= 'Test Description', start_date= '25.01.2024', end_date= '26.10.2024', author=self.user)
        self.client.post(reverse('journey_join', args= [self.journey.id]))
        assert self.user in self.journey.participants.all()
        response= self.client.post(reverse('journey_leave', args=[self.journey.id]))
        self.journey.refresh_from_db()
        self.assertNotIn(self.user, self.journey.participants.all())
        self.assertEqual(response.status_code, 302)



    def test_journey_list_view(self):
        response= self.client.get(reverse('journey_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/journey_list.html')


    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_details.html')


    def test_post_edit_view(self):
        response = self.client.post(reverse('post_edit', args=[self.post.id]), {
            'title': 'Updated title',
            'content': 'Updated content'})
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated title')
        self.assertEqual(self.post.content, 'Updated content')
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post.id]))
        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(response.status_code, 302)








