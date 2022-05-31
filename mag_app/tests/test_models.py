from django.test import TestCase
from mag_app.models import Post
from django.contrib.auth.models import User


class TestModels(TestCase):

    def test_post_status_defautls_to_draft(self):
        user = User.objects.create(username='testname')
        article = Post.objects.create(
            title='article1',
            author=user
        )
        self.assertFalse(article.status)
