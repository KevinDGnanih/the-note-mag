
from django.test import TestCase
from mag_app.models import Post, Comment
from django.contrib.auth.models import User


class TestModels(TestCase):

    def test_post_status_defaults_to_draft(self):
        user = User.objects.create(username='testname')
        article = Post.objects.create(
            title='article1',
            author=user
        )
        self.assertFalse(article.status)

    def test_comment_approved_defaults_to_false(self):
        user = User.objects.create(username='testname')
        article = Post.objects.create(
            title='article1',
            author=user
        )
        comment = Comment.objects.create(
            post=article,
            body='article comment',
        )
        self.assertFalse(comment.approved)

    def test_post_string_method_returns_title(self):
        user = User.objects.create(username='testname')
        article = Post.objects.create(
            title='article1',
            author=user
        )
        self.assertEquals(str(article), 'article1')

    def test_comment_string_method_returns_comment(self):
        user = User.objects.create(username='testname')
        article = Post.objects.create(
            title='article1',
            author=user
        )
        comment = Comment.objects.create(
            post=article,
            name=user,
            body='article comment',
        )
        self.assertEquals(str(comment), 'Comment article comment by testname')
