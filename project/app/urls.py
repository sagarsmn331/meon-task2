from app import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('User',views.UserViewSet, basename='User')
urlpatterns = router.urls