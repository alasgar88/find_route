
from django.urls import path
from .views import *

urlpatterns = [
    path('', CityListView.as_view(), name="city_list"),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='city_update'),
    path('add/', CityCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='city_delete'),
]
