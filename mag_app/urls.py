""" URLS file for the mag_app """
from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('search', views.search, name='search'),
    path('category/<str:cats>', views.category_posts, name='category'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('edit_post/<slug:slug>', views.EditPost.as_view(), name='edit_post'),
    path('<slug:slug>/delete', views.DeletePost.as_view(), name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
