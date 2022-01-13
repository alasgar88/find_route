from django.shortcuts import render
from routes.utils import get_routes
from .forms import RouteForm
from django.contrib import messages


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, "Not data for search")
        return render(request, 'routes/home.html', {'form': form})
