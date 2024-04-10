from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apis.urls')),
    path('', include('django_prometheus.urls')),
]
