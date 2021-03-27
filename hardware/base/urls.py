from django.urls import path

from base.views import HardwaresListView, HardwaresDetailView
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('hardwares/', HardwaresListView.as_view(), name='hardware_list'),
    path('hardwares/<int:pk>', HardwaresDetailView.as_view(), name='hardware_detail'),
]
