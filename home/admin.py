from django.contrib import admin
from home.models import  Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at', 'updated_at','uid','blog_text','main_image')
    readonly_fields = ('created_at', 'updated_at','uid')

admin.site.register(Blog, BlogAdmin)
