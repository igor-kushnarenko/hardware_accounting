from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from base import views

router = routers.DefaultRouter()
router.register(r'hardware', views.HardwareViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('users/', include('users.urls')),
    path('router/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
