from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView

from base.models import Hardware


def index_view(request):
    return render(request, 'base/index.html', {})


class HardwaresListView(generic.ListView):
    model = Hardware
    template_name = 'hardware_list.html'
    context_object_name = 'hardware_list'
    queryset = Hardware.objects.order_by('place', '-status')


class HardwaresDetailView(generic.DetailView):
    model = Hardware

