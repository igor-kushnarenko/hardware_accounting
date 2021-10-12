from django.urls import path

from base.views import HardwaresListView, HardwaresDetailView, \
    AddHardwaresFormView, EditHardwaresView, delete, edit_repair, delete_repair

urlpatterns = [
    path('', HardwaresListView.as_view(), name='hardware_list'),
    path('add', AddHardwaresFormView.as_view(), name='add_hardware'),
    path('hardwares/<int:pk>/edit', EditHardwaresView.as_view(), name='hardware_edit'),
    path('hardwares/<int:pk>', HardwaresDetailView.as_view(), name='hardware_detail'),
    path('hardwares/edit_repair/<int:id>', edit_repair),
    path('hardwares/delete/<int:id>', delete),
    path('hardwares/delete_repair/<int:id>', delete_repair),
]
