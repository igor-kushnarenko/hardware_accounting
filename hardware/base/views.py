from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import FormView
from django.views.generic.base import TemplateView, View

from base.models import Hardware, Repair
from base.form import HardwareForm, RepairForm


def index_view(request):
    return render(request, 'base/index.html', {})


class HardwaresListView(generic.ListView):
    model = Hardware
    template_name = 'hardware_list.html'
    context_object_name = 'hardware_list'
    queryset = Hardware.objects.order_by('place', '-status')


class HardwaresDetailView(View):
    def get(self, request, pk):
        hardware = Hardware.objects.get(id=pk)
        hardware_id = pk
        repairs = Repair.objects.filter(hardware=hardware_id)
        repair_form = RepairForm()
        return render(
            request,
            'base/hardware_detail.html',
            context={
                'hardware': hardware,
                'hardware_id': hardware_id,
                'repairs': repairs,
                'repair_form': repair_form,
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
    success_url = 'hardwares'

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
