from django.contrib import admin

from base.models import Hardware, Type, Manufacturer, Status, Place, Repair


def make_repair_status_inactive(modeladmin, request, queryset):
    queryset.update(status=False)


def make_repair_status_active(modeladmin, request, queryset):
    queryset.update(status=True)


make_repair_status_inactive.short_description = 'Не в ремонте'
make_repair_status_active.short_description = 'В ремонте'


class RepairInLine(admin.TabularInline):
    model = Repair
    max_num = 3
    extra = True


@admin.register(Hardware)
class HardwareAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'model', 'type',
                    'serial', 'place', 'status']
    list_display_links = ['manufacturer', 'model']
    list_filter = ['place', 'status', 'type', 'manufacturer']
    list_per_page = 50
    save_as = True
    inlines = [RepairInLine]
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
    sortable_by = ['name']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ['date_repair', 'hardware',
                    'problem', 'contractor',
                    'end_date_repair', 'result',
                    'cost', 'status']
    list_editable = ['end_date_repair']
    list_filter = ['status']
    actions = [make_repair_status_inactive, make_repair_status_active]