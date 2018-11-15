from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.file_list, name='file_list'),
    path('upload/',views.uploading,name='uploading'),
    # path('login/',views.my_view),

]