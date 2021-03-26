from django.urls import path

from base.views import HardwaresListView
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('hardwares/', HardwaresListView.as_view(), name='hardware_list'),
]
