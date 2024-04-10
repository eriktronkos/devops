from django.conf.urls import url
from django.urls import path

from .views import TodoViewSet, HealthCheckView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todos')
urlpatterns = router.urls + [url(r'healthcheck/', HealthCheckView.as_view())]
