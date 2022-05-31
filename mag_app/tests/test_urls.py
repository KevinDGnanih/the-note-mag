from django.test import SimpleTestCase
from django.urls import reverse, resolve
from magg_app.views import PostList, PostDetail, PostLike, about, search


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_search_url_resolves(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    def test_detail_url_resolves(self):
        url = reverse('post_detail', args=['test-slug'])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    def test_like_url_resolves(self):
        url = reverse('post_like', args=['test-slug'])
        self.assertEquals(resolve(url).func.view_class, PostLike)