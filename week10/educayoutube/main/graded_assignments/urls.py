# from django.urls import path
# from main.views import GradedAssignmentListView, GradedAssignmentCreateView
#
# urlpatterns = [
#     path('', GradedAssignmentListView.as_view()),
#     path('create/', GradedAssignmentCreateView.as_view()),
# ]
from rest_framework.routers import DefaultRouter
from main.views import AssignmentViewSet

router = DefaultRouter()
router.register(r'', AssignmentViewSet, base_name='assignments')
urlpatterns = router.urls