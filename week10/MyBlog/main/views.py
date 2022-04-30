from datetime import timedelta
from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsPostAuthor
from rest_framework.pagination import PageNumberPagination


from .serializer import CategorySerializer, PostSerializer, ImageSerializer
from .models import Category, Post, Image
# Create your views here.

# @api_view(['GET', 'POST'])
# def categories(request):
#     if request.method =='GET':
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True) #many=True, so that the seriazlier holds muplitple objects
#         return Response(serializer.data)
#     else:
#         return Response({"message": "Message of categories"})
#
# class PostListView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializers = PostSerializer(posts, many=True)
#         return Response(serializers.data)
#     def post(self, request):
#         post = request.data
#         print(post)
#         serializer = PostSerializer(data=post)
#         if serializer.is_valid(raise_exception=True):
#             post = serializer.save()
#         return Response(serializer.data)


# list of categories

class MyPaginationClass(PageNumberPagination):
    page_size = 3

    def get_paginated_response(self, data):
        for i in range(self.page_size):
            text = data[i]['text']
            data[i]['text'] = text[:10] + '...'



        return super().get_paginated_response(data)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ] #everyone can view the categories


class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ] #only logged in users can view the posts
    pagination_class = MyPaginationClass
    def get_permissions(self):
        print(self.action)
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsPostAuthor, ] #only the authors of the post can update and delete the post
        else:
            permissions = [IsAuthenticated, ]
        return [permission() for permission in permissions]

    #filtering using queryset by the date
    def get_queryset(self):
        queryset = super().get_queryset()
        days_count = int(self.request.query_params.get('days', default=0))
        if days_count>0:
            start_date = timezone.now() - timedelta(days=days_count)
            queryset = queryset.filter(created_at__gte=start_date)
        return queryset

    #filtering by my posts using action decorator, url -> v1/api/posts/own/
    @action(detail=False, methods=['get'])
    def own(self, request, pk=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(author=request.user)
        serializer = PostSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        print(request.query_params)
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(title__icontains=q)|Q(text__icontains=q))
        serializer = PostSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_context(self):
        return {'request': self.request}




#
# # PostView and PostCreate
# class PostView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# #PostDetailView
# class PostDetailView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostUpdateView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDeleteView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#



