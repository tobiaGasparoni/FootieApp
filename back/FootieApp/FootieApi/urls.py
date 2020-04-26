from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'packages', views.PackageViewSet)
router.register(r'parents', views.ParentViewSet)
router.register(r'training_days', views.TrainingDayViewSet)
router.register(r'reports', views.ReportViewSet)
router.register(r'access_code', views.AdminViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
