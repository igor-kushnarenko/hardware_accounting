import xlwt
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import FormView
from django.views.generic.base import TemplateView, View
from rest_framework import viewsets, permissions

from base.models import Hardware, Repair, Place, Type, Manufacturer, Status
from base.form import HardwareForm, RepairForm
from base.serializers import HardwareSerializer


def index_view(request):
    return render(request, 'base/index.html', {})


class HardwaresListView(generic.ListView):
    model = Hardware
    template_name = 'hardware_list.html'
    context_object_name = 'hardware_list'
    queryset = Hardware.objects.order_by('type', 'status')

    def get_context_data(self, **kwargs):
        context = super(HardwaresListView, self).get_context_data(**kwargs)
        context['count'] = Hardware.objects.count()
        return context


class HardwaresDetailView(View):
    def get(self, request, pk):
        hardware = Hardware.objects.get(id=pk)
        hardware_id = pk
        repairs = Repair.objects.filter(hardware=hardware_id)
        return render(
            request,
            'base/hardware_detail.html',
            context={
                'hardware': hardware,
                'hardware_id': hardware_id,
                'repairs': repairs,
            }
        )

    def post(self, request, pk):
        repair_form = RepairForm(request.POST)
        if repair_form.is_valid():
            repairs = repair_form.save(commit=False)
            repairs.hardware_id = pk
            repairs.save()
            return HttpResponseRedirect(request.path_info)


class AddHardwaresFormView(FormView):
    template_name = 'base/add_hardware.html'
    form_class = HardwareForm
    success_url = '/'

    def form_valid(self, form):
        Hardware.objects.create(**form.cleaned_data)
        return super(AddHardwaresFormView, self).form_valid(form)


class EditHardwaresView(View):
    def get(self, request, pk):
        hardware = Hardware.objects.get(id=pk)
        hardware_form = HardwareForm(instance=hardware)
        return render(
            request,
            'base/edit_hardware.html',
            context={'hardware_form': hardware_form, 'pk': pk}
        )

    def post(self, request, pk):
        hardware = Hardware.objects.get(id=pk)
        hardware_form = HardwareForm(request.POST, instance=hardware)

        if hardware_form.is_valid():
            hardware.save()
        return render(
            request,
            'base/edit_hardware.html',
            context={'hardware_form': hardware_form, 'pk': pk}
        )

# для формы с подставлением данных
# def edit_repair(request, id):
#     try:
#         repair = Repair.objects.get(id=id)
#         hardware_id = repair.hardware.id
#         if request.method == "POST":
#             repair.date_repair = request.POST.get("date_repair")
#             repair.problem = request.POST.get("problem")
#             repair.contractor = request.POST.get("contractor")
#             repair.end_date_repair = request.POST.get("end_date_repair")
#             repair.result = request.POST.get("result")
#             repair.cost = request.POST.get("cost")
#             repair.status = request.POST.get("status")
#             repair.save()
#             return HttpResponseRedirect(f"/hardwares/{hardware_id}")
#         else:
#             return render(request, "base/edit_repair_test.html", {"repair": repair})
#     except Hardware.DoesNotExist:
#         return HttpResponseNotFound("<h2>Hardware not found</h2>")


class EditRepairView(FormView):
    """
    Метод редактирования ремонтов
    """
    template_name = 'base/edit_repair.html'
    form_class = RepairForm
    success_url = '/'

    def form_valid(self, form):
        Repair.objects.create(**form.cleaned_data)
        return super(EditRepairView, self).form_valid(form)


# функция удаления ремонтов
def delete_repair(request, id):
    try:
        repair = Repair.objects.get(id=id)
        hardware_id = repair.hardware.id
        repair.delete()
        return HttpResponseRedirect(f'/hardwares/{hardware_id}')
    except Hardware.DoesNotExist:
        return HttpResponseNotFound("<h2>Repair not found</h2>")


# функция удаления приборов
def delete(request, id):
    try:
        hardware = Hardware.objects.get(id=id)
        hardware.delete()
        return HttpResponseRedirect("/")
    except Hardware.DoesNotExist:
        return HttpResponseNotFound("<h2>Hardware not found</h2>")


class PlacesHardwaresView(View):
    def get(self, request, id):
        place = Place.objects.get(pk=id)
        hardwares = Hardware.objects.filter(place=id)
        count = place.hardware.count() # счетчик количества записей
        return render(request, 'base/places.html', context={
            'place': place,
            'hardwares': hardwares,
            'count': count,
        })


def export_hardwares_xls(request, id):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="hardwares.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Оборудование')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Тип', 'Производитель', 'Модель', 'Серийный номер', 'Расположение', 'Состояние']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Hardware.objects.filter(place=id).values_list(
        'type',
        'manufacturer',
        'model',
        'serial',
        'place',
        'status',
    )

    for row in rows:
        row_num += 1
        type = row[0]
        manufacturer = row[1]
        model = row[2]
        serial = row[3]
        place = row[4]
        status = row[5]

        ws.write(row_num, 0, Type.objects.get(id=type).name, font_style)
        ws.write(row_num, 1, Manufacturer.objects.get(id=manufacturer).name, font_style)
        ws.write(row_num, 2, model, font_style)
        ws.write(row_num, 3, serial, font_style)
        ws.write(row_num, 4, Place.objects.get(id=place).name, font_style)
        ws.write(row_num, 5, Status.objects.get(id=status).name, font_style)

    wb.save(response)
    return response


def export_all_hardwares_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="hardwares.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Оборудование')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Тип', 'Производитель', 'Модель', 'Серийный номер', 'Расположение', 'Состояние']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Hardware.objects.all().values_list(
        'type',
        'manufacturer',
        'model',
        'serial',
        'place',
        'status',
    )

    for row in rows:
        row_num += 1
        type = row[0]
        manufacturer = row[1]
        model = row[2]
        serial = row[3]
        place = row[4]
        status = row[5]

        ws.write(row_num, 0, Type.objects.get(id=type).name, font_style)
        ws.write(row_num, 1, Manufacturer.objects.get(id=manufacturer).name, font_style)
        ws.write(row_num, 2, model, font_style)
        ws.write(row_num, 3, serial, font_style)
        ws.write(row_num, 4, Place.objects.get(id=place).name, font_style)
        ws.write(row_num, 5, Status.objects.get(id=status).name, font_style)

    wb.save(response)
    return response


class HardwareViewSet(viewsets.ModelViewSet):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer
    permission_classes = [permissions.IsAuthenticated]