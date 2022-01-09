
from django.urls import path
from .views import *

urlpatterns = [
    path('', TrainListView.as_view(), name="train_list"),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='train_detail'),
    path('add/', TrainCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='train_update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='train_delete'),
]
