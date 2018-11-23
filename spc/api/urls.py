from django.urls import include, path
from django.conf.urls import url

from . import views

urlpatterns = [
    # path('', views.ListTodo.as_view()),
    # path('<int:pk>/', views.DetailTodo.as_view()),
    path('get_time_info/',views.get_time_info),
    path('update_time_info/',views.update_time_info),
    url(r'^uploadfile/(?P<parent_id>[0-9]+)/$',views.uploadfile,name='uploadfile'),
    url(r'^createfolder/(?P<parent_id>[0-9]+)/$',views.createfolder,name='createfolder'),
    url(r'^filedownload/(?P<parent_id>[0-9]+)/$',views.filedownload,name='filedownload'),
    url(r'^folderlist/(?P<parent_id>[0-9]+)/$',views.folderlist,name='folderlist'),
    path('abc/',views.abc),
    path('rootfinder/',views.rootfinder),
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]