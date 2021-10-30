from django.urls import path

from base import views

urlpatterns = [
    path('', views.HardwaresListView.as_view(), name='hardware_list'),
    path('add', views.AddHardwaresFormView.as_view(), name='add_hardware'),
    path('hardwares/<int:pk>/edit', views.EditHardwaresView.as_view(), name='hardware_edit'),
    path('hardwares/<int:pk>', views.HardwaresDetailView.as_view(), name='hardware_detail'),
    path('hardwares/edit_repair/<int:id>', views.EditRepairView.as_view(), name='edit_repair'),
    path('hardwares/delete_repair/<int:id>', views.delete_repair, name='delete_repair'),
    path('hardwares/delete/<int:id>', views.delete),
    path('hardwares/places/<int:id>', views.PlacesHardwaresView.as_view(), name='places_hardwares'),
    path('export_hardwares_xls/<int:id>', views.export_hardwares_xls, name='export_hardwares_xls'),
    path('export_hardwares_xls/all', views.export_all_hardwares_xls, name='export_all_hardwares_xls'),
]
