"""aikaed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from courses.views import SubjectListView
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('v1/api/subjects/', SubjectListView.as_view(), name='subjects_list'),
# ]
#

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from courses.views import SubjectListView, CoursesViewSet, ModuleView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('courses', CoursesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/api/subjects/', SubjectListView.as_view(), name='categories_list'),
    path('v1/api/account/', include('account.urls')),
    path('v1/api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # для того чтобы он видел картинки в папке media
