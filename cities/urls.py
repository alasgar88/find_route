
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="city_list"),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
]
