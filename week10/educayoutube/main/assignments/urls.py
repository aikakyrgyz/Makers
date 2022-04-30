from rest_framework.routers import DefaultRouter
from main.views import AssignmentViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'', AssignmentViewSet, base_name='assignments')
urlpatterns = router.urls