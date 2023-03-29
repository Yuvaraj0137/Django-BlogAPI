from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'blog_text', 'main_image', 'user', 'created_at', 'uid')

class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ( 'title', 'blog_text', 'main_image', 'user', 'uid', 'updated_at') 

        