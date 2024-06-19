from users.forms import CustomUserCreationForm
from users.models import CustomUser
import pytest
from django.test import TestCase
from blog.forms import PostForm, JourneyForm, CommentForm
# from blog.models import Post, Journey, Comment

class PostFormTest(TestCase):
    def test_valid_form(self):
        data={
            'title': 'title',
            'content': 'Content',
            'location': 'Location'
        }
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())




    def test_invalid_form(self):

        data= {
            'title': '',
            'content': 'Content',
            'location': 'Location'
        }
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())


class JourneyFormTest(TestCase):
    def test_valid_form(self):
        data={
            'title': 'Journey',
            'description': 'Test Description',
            'start_date': '23.06.1987',
            'end_date': 'infinity'
        }
        form= JourneyForm(data=data)
        self.assertTrue(form.is_valid())



    def test_invalid_form(self):
        data={
            'title': '',
            'description': 'Test Description',
            'start_date': '23.06.1987',
            'end_date': 'infinity'
        }
        form= JourneyForm(data=data)
        self.assertFalse(form.is_valid())




class CommentFormTest(TestCase):

    def test_valid_form(self):
        data= {
            'text': 'Comment'
        }
        form= CommentForm(data= data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'text': ''
        }
        form= CommentForm(data= data)
        self.assertFalse(form.is_valid())




@pytest.mark.django_db
def test_create_user():
    user =  CustomUser.objects.create_user(
        username= 'testuser',
        password='testpass123'
    )

    assert user.username == 'testuser'





class CustomUserCreationFormTest(TestCase):

    def test_form_valid(self):
        form_data= {
            'username': 'testuser',
            'email':'testuser@anything.com',
            'password1': 'testpass123',
            'password2':'testpass123',
        }
        form = CustomUserCreationForm(data= form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_due_to_existing_username(self):
        CustomUser.objects.create_user(username='testuser', email='testuser@example.com', password='testpass123')
        form_data= {
            'username':'testuser',
            'email': 'newuser@anything.com',
            'password1':'testpass123',
            'password2':'testpass123',
        }
        form= CustomUserCreationForm(data= form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
    def test_form_invalid_due_to_existing_email(self):
        CustomUser.objects.create_user(username='testuser', email='testuser@anything.com', password='testpass123')
        form_data= {
            'username':'newuser',
            'email':'testuser@anything.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        form=CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

