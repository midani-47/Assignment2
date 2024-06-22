from django.test import TestCase
from blog.models import Post, Journey, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class PostModelTest(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='testuser', password='testpass123', email='testuser@something.com')

    def test_create_post(self):
        post = Post.objects.create(title='Poster', content='Content', author=self.user)
        self.assertEqual(post.title, 'Poster')
        self.assertEqual(post.content, 'Content')
        self.assertEqual(post.author, self.user)


    def test_like_post(self):
        post= Post.objects.create(title='Poster', content='Content', author=self.user)
        post.likes.add(self.user)
        self.assertEqual(post.likes.count(), 1)
    def test_unlike_post(self):
        post= Post.objects.create(title='Poster', content='Content', author=self.user)
        post.likes.add(self.user)
        post.likes.remove(self.user)
        self.assertEqual(post.likes.count(), 0)

    def test_post_delete(self):
        post= Post.objects.create(title='Poster', content='Content', author=self.user)
        post.delete()
        self.assertEqual(Post.objects.count(), 0)

    def test_post_edit(self):
        post=Post.objects.create(title='Test post', content='Test content', author=self.user)
        post.title='Updated Title'
        post.save()
        self.assertEqual(post.title, 'Updated Title')





class JourneyModelTest(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='testuser', password='testpass123', email='testuser@something.com')

    def test_create_journey(self):
        journey=Journey.objects.create(title='Journey', description='Test Description', start_date='23/06/1987', end_date='now', author=self.user)
        self.assertEqual(journey.title, 'Journey')
        self.assertEqual(journey.description, 'Test Description')
        self.assertEqual(journey.author, self.user)


class CommentModelTest(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='testuser', password='testpass123', email='testuser@something.com')
        self.post= Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_create_comment(self):
        comment= Comment.objects.create(post=self.post, author=self.user, text='Test Comment')
        self.assertEqual(comment.text, 'Test Comment')
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.post, self.post)
