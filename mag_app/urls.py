""" URLS file for the mag_app """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]
