from django.contrib import admin
from django.urls import path
from home.views import BlogView, PublicBlogView

urlpatterns = [
    path('blogs/', PublicBlogView.as_view()),
    path('my_blogs/', BlogView.as_view()),
]