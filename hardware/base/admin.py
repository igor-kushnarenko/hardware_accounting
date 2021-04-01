from django.contrib import admin

from base.models import Hardware, Type, Manufacturer, Status, Place, Repair


@admin.register(Hardware)
class HardwareAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'manufacturer', 'model',
                    'serial', 'place', 'status']
    list_filter = ['place', 'status', 'type']
    fieldsets = (
        ('Основные сведения', {
            'fields': ('type', 'manufacturer', 'model')
        }),
        ('Внутренние сведения', {
            'fields': ('serial', 'place', 'comment', 'status')
        }),
    )


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Repair)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['date_repair', 'problem',
                    'contractor', 'end_date_repair',
                    'result', 'cost']