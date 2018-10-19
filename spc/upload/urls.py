from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_list, name='file_list'),
]