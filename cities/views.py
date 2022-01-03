from typing_extensions import ParamSpecArgs
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from .models import City

__all__ = (
    'home', 'CityDetailView',
)


def home(request, pk=None):
    if pk:
        #city = City.objects.filter(id=pk).first()
        city = get_object_or_404(City, id=pk)
        context = {"object": city}
        return render(request, 'cities/detail.html', context)

    qs = City.objects.all()
    context = {"objects_list": qs}
    return render(request, 'cities/city_list.html', context)


class CityDetailView(DetailView):

    queryset = City.objects.all()
    template_name = 'cities/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return context
