from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # path('view/', views.file_list, name='file_list'),
    # path('upload/',views.uploading,name='uploading'),
    url(r'^newfolder/(?P<form_id>[0-9]+)/$',views.make_new_folder,name='make_new_folder'),
    url(r'^newfolder/$',views.rootfinder),
    url('search/',views.search),
    url(r'filedelete/(?P<file_id>[0-9]+)/$',views.filedelete,name = 'delete_file'),
    url(r'folderdelete/(?P<folder_id>[0-9]+)/$',views.folderdelete,name = 'delete_folder'),
    url(r'^fileview/(?P<file_id>[0-9]+)/$',views.fileview,name='fileview'),
    url(r'^filedownload/(?P<file_id>[0-9]+)/$',views.filedownload,name='filedownload')
    # path('login/',views.my_view),

]