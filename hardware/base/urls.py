from django.contrib import admin
from django.urls import path, include

from .views import HelloView

urlpatterns = [
    path('', HelloView.as_view(), name='hello')
]
