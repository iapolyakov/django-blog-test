from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class PostMethodTests(TestCase):

    def setUp(self):
        author = User.objects.create_user(username='name',
                                          email='name@mail.ru',
                                          password='namepass')
        Post.objects.create(author=author, title='Test', text='Desc')

    def test_post_publish(self):
        """sets published_date"""
        post = Post.objects.get(title='Test')
        self.assertIsNone(post.published_date)
        post.publish()
        self.assertIsNotNone(post.published_date)

    def test_approved_comments(self):
        """returns only aproved comments"""
        post = Post.objects.get(title='Test')
        comment = post.comments.create(author='name', text='comment')
        self.assertQuerysetEqual(post.approved_comments(), [])
        comment.approve()
        self.assertQuerysetEqual(post.approved_comments(), ['<Comment: comment>'])





