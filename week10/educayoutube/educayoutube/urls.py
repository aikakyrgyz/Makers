"""educayoutube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include, re_path
from main.views import QuestionViewSet
from django.views.generic import TemplateView
router = DefaultRouter()
router.register('questions', QuestionViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')), #https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('assignments/', include('main.assignments.urls')),
    path('graded-assignments/', include('main.graded_assignments.urls')),
    path('users/', include('user.urls')),
    path('api/', include(router.urls))
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
