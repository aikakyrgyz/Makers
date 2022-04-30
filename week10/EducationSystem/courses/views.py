from django.shortcuts import render

from .serializers import SubjectSerializer, ModuleSerializer, CourseSerializer
from .models import Subject, Course, Module
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .permissions import IsCourseAuthor


# Create your views here.
class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny, ] #everyone can view the categories


class ModuleView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny, ] #only logged in users can view the posts
    # pagination_class = MyPaginationClass
    def get_permissions(self):
        print(self.action)
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsCourseAuthor, ] #only the authors of the post can update and delete the post
        else:
            permissions = [IsAuthenticated, ]
        return [permission() for permission in permissions]

    def get_serializer_context(self):
        return {'request': self.request}

