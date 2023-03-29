from rest_framework.views import APIView
from rest_framework.response import Response
from home.serializers import BlogSerializer, BlogCreateSerializer, BlogUpdateSerializer
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.paginator import Paginator
from home.models import Blog
from django.db.models import Q
from datetime import datetime
import json
 


class PublicBlogView(APIView):

    def get(sef, request):
        try:
            blogs = Blog.objects.all().order_by('?')
            if request.GET.get('search'):
                search = request.GET.get('search')
                blogs = blogs.filter(Q(title__icontains = search) | Q(blog_text__icontains = search))
 
            paginator = Paginator(blogs, 5)
            page_number = request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            serializer = BlogSerializer(page, many=True)
             
            return Response({
                'data' : serializer.data,
                'message' : 'blogs fetched successfully'
            }, status= status.HTTP_201_CREATED)
        except Exception as e :
          print(e)
          return Response({
            'data': {},
            'message' : 'Something went wrong or invalid page'
          }, status = status.HTTP_400_BAD_REQUEST)

 

class BlogView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            blogs = Blog.objects.filter(user = request.user)

            if request.GET.get('search'):
             search = request.GET.get('search')
             blogs = blogs.filter(Q(title__icontains = search) | Q(blog_text__icontains = search))

            serializer = BlogSerializer(blogs, many = True)

            return Response({
                'data' : serializer.data,
                'message' : 'blogs fetched successfully'
            }, status= status.HTTP_201_CREATED)
        except Exception as e :
          print(e)
          return Response({
            'data': {},
            'message' : 'something went wrong'
          }, status = status.HTTP_400_BAD_REQUEST)
        


    def post(self, request):
        try:
            data = request.data.copy()
            data['user'] = request.user.id
            print(data)
            print(request.user)
            serializer =  BlogCreateSerializer(data = data)
            if not serializer.is_valid():
               return Response({
                    'data': serializer.errors,
                    'message' : 'Something Went Wrong'
                    })
            
            serializer.save()

            return Response({
                   'data': serializer.data,
                    'message' : 'Blog created successfully'
                    },status = status.HTTP_201_CREATED)
             
             
        except Exception as e :
            print(e)
            return Response({
                'data': request.data,
                'message' : 'something went wrong'
            }, status = status.HTTP_400_BAD_REQUEST)
        
        
    def patch(self, request):
        try:
            data = request.data.copy()
            now = datetime.now()
            date_only = now.date()
            #data['updated_at'] =  date_only
            print(date_only)

            blog = Blog.objects.get(uid = data['uid'])

            if not blog:
                return Response({
                'data': {},
                'message' : 'invalid blog uid'
            }, status = status.HTTP_400_BAD_REQUEST)
            
            if request.user != blog.user :
                return Response({
                  'data': {},
                  'message' : 'you are not autherized to do this'
            }, status = status.HTTP_400_BAD_REQUEST)
               

            serializer =  BlogUpdateSerializer(blog,  data = data, partial = True)
            

            if not serializer.is_valid():
               return Response({
                 'data': serializer.errors,
                 'message' : 'Something Went Wrong'
            })
            
            serializer.save()
            return Response({
                'data': serializer.data,
                'message' : 'Blog updated successfully'
            },status = status.HTTP_201_CREATED)
        

        except Exception as e :
            print(e)
            return Response({
                'data': request.data,
                'message' : 'something went wrong'
            }, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        try:
            data = request.data

            blog = Blog.objects.get(uid = data['uid'])

            if not blog:
                return Response({
                'data': {},
                'message' : 'invalid blog uid'
            }, status = status.HTTP_400_BAD_REQUEST)
            
            if request.user != blog.user :
                return Response({
                  'data': {},
                  'message' : 'you are not autherized to do this'
            }, status = status.HTTP_400_BAD_REQUEST)  

            serializer = BlogSerializer(blog)

            blog.delete()   

            return Response({
                'data': serializer.data,
                'message' : 'Blog deleted successfully'
            },status = status.HTTP_201_CREATED)  

        except Exception as e :
            print(e)
            return Response({
                'data': {},
                'message' : 'something went wrong'
            }, status = status.HTTP_400_BAD_REQUEST)      
        

        

        
    
        
         
             
