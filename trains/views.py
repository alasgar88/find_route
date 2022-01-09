from django.core import paginator
from .models import Train
from cities.forms import HtmlForm, CityForm
from trains.forms import TrainForm
from typing_extensions import ParamSpecArgs
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


__all__ = (
    'home', 'TrainListView', 'TrainDetailView',
    'TrainCreateView', 'TrainUpdateView', 'TrainDeleteView',
)


def home(request, pk=None):
    qs = Train.objects.all()
    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'trains/home.html', context)


class TrainListView(ListView):
    model = Train
    template_name = 'trains/home.html'
    paginate_by = 3


class TrainDetailView(DetailView):

    model = Train
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    template_name = 'trains/create.html'
    form_class = TrainForm
    success_url = reverse_lazy('trains:train_list')
    obj = ''

    def form_valid(self, form):
        self.obj = form.instance.name
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return f"Train { self.obj} was created succesfully"


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:train_list')

    def get_success_message(self, cleaned_data):
        obj = super().get_object()
        return f"Train { obj.name }was updated succesfully"


class TrainDeleteView(DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:train_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        return obj

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.add_message(request, messages.SUCCESS,
                             f"Train {obj.name} was deleted succesfully")
        return super().post(request, *args, **kwargs)
