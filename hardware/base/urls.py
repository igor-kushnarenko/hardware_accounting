from django.urls import path

from base.views import HardwaresListView, HardwaresDetailView, \
    AddHardwaresFormView, EditHardwaresView
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('hardwares/', HardwaresListView.as_view(), name='hardware_list'),
    path('add', AddHardwaresFormView.as_view(), name='add_hardware'),
    path('hardwares/<int:pk>/edit', EditHardwaresView.as_view(), name='hardware_edit'),
    path('hardwares/<int:pk>', HardwaresDetailView.as_view(), name='hardware_detail'),
]
