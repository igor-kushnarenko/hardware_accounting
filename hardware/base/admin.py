from django.contrib import admin

from base.models import Hardware, Type, Manufacturer, Status, Place, Repair


def make_repair_status_inactive(modeladmin, request, queryset):
    queryset.update(status=False)


def make_repair_status_active(modeladmin, request, queryset):
    queryset.update(status=True)


def move_to_marini(modeladmin, request, queryset):
    queryset.update(place=1)


def move_to_normandia(modeladmin, request, queryset):
    queryset.update(place=2)


def move_to_saint_michele(modeladmin, request, queryset):
    queryset.update(place=3)


def move_to_scene(modeladmin, request, queryset):
    queryset.update(place=4)


def move_to_beach(modeladmin, request, queryset):
    queryset.update(place=5)


def move_to_mobile(modeladmin, request, queryset):
    queryset.update(place=6)


def move_to_dicso(modeladmin, request, queryset):
    queryset.update(place=7)


def move_to_sclad(modeladmin, request, queryset):
    queryset.update(place=8)


def move_to_mediaclass(modeladmin, request, queryset):
    queryset.update(place=9)


make_repair_status_inactive.short_description = 'Не в ремонте'
make_repair_status_active.short_description = 'В ремонте'
move_to_marini.short_description = 'В Марини'
move_to_normandia.short_description = 'В Нормандию'
move_to_saint_michele.short_description = 'В Сан-Мишель'
move_to_scene.short_description = 'На сцену'
move_to_beach.short_description = 'На пляж'
move_to_mobile.short_description = 'Мобильный'
move_to_dicso.short_description = 'В Диско-бар'
move_to_sclad.short_description = 'На склад'
move_to_mediaclass.short_description = 'В Медиакласс'



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
    actions = [
        move_to_mediaclass, move_to_beach, move_to_mobile,
        move_to_normandia, move_to_scene, move_to_dicso,
        move_to_sclad, move_to_saint_michele, move_to_marini,
    ]
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
    list_display = ['id', 'name']


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ['date_repair', 'hardware',
                    'problem', 'contractor',
                    'end_date_repair', 'result',
                    'cost', 'status']
    list_editable = ['end_date_repair']
    list_filter = ['status']
    actions = [make_repair_status_inactive, make_repair_status_active]