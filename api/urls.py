from django.urls import path, include 

urlpatterns = [
    path('blog_account/', include('blog_account.urls')),
    path('home/', include('home.urls')),
]