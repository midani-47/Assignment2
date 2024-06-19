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
        self.user=User.objects.create_user(username='testuser',password= 'testpass123',email= 'testuser@anything.com')
        self.client.login(username= 'testuser',password= 'testpass123')


    def test_login_view(self):
        response=self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)


    def test_logout_view(self):
        response=self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
    def test_register_view(self):
        response= self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')


class BlogViewTests(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(username= 'testuser',password = 'password',email= 'testuser@anything.com')
        self.client.force_login(self.user)
        self.client.login(username= 'testuser',password= 'password')
        self.post = Post.objects.create(title= 'Test Post',content= 'Test Content',author=self.user)


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
        self.journey.refresh_from_db()  # Refresh to get the latest state
        self.assertNotIn(self.user, self.journey.participants.all())
        self.assertEqual(response.status_code, 302)



    def test_journey_list_view(self):
        response= self.client.get(reverse('journey_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/journey_list.html')








