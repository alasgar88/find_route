from django.core import paginator
from .models import City
from .forms import CityForm
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


__all__ = (
    'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView', 'CityListView',
)


# def home(request, pk=None):
#     # if pk:
#     #     #city = City.objects.filter(id=pk).first()
#     #     city = get_object_or_404(City, id=pk)
#     #     context = {"object": city}
#     #     return render(request, 'cities/detail.html', context)

#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data)

#     form = CityForm()
#     qs = City.objects.all()
#     lst = Paginator(qs, 3)
#     page_number = request.GET.get('page')
#     page_obj = lst.get_page(page_number)
#     context = {"page_obj": page_obj, "form": form}
#     return render(request, 'cities/city_list.html', context)


class CityListView(ListView):
    model = City
    template_name = 'cities/city_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context


class CityDetailView(DetailView):

    model = City
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    template_name = 'cities/create.html'
    form_class = CityForm
    success_url = reverse_lazy('cities:city_list')
    obj = ''

    def form_valid(self, form):
        self.obj = form.instance.name
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return f"City { self.obj} was created succesfully"


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:city_list')

    def get_success_message(self, cleaned_data):
        obj = super().get_object()
        return f"City { obj.name }was updated succesfully"


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:city_list')

    def post(self, request, *args, **kwargs):
        obj = super().get_object()
        messages.add_message(request, messages.SUCCESS,
                             f"City {obj.name} was deleted succesfully")
        return super().post(request, *args, **kwargs)
