from django.shortcuts import render
from django.views import generic
from django.views.generic import FormView
from django.views.generic.base import TemplateView, View

from base.models import Hardware
from base.form import HardwareForm


def index_view(request):
    return render(request, 'base/index.html', {})


class HardwaresListView(generic.ListView):
    model = Hardware
    template_name = 'hardware_list.html'
    context_object_name = 'hardware_list'
    queryset = Hardware.objects.order_by('place', '-status')


class HardwaresDetailView(generic.DetailView):
    model = Hardware


class AddHardwaresFormView(FormView):
    template_name = 'base/add_hardware.html'
    form_class = HardwareForm
    success_url = 'hardwares'

    def form_valid(self, form):
        Hardware.objects.create(**form.cleaned_data)
        return super(AddHardwaresFormView, self).form_valid(form)

# TODO добавить возможность редактирования оборудования
# TODO добавить добавление ремонта на странице детальной информации
# добавить кнопку Редактировать и Удалить на странице детальной информации