from django.shortcuts import render, redirect
from django.utils import timezone
from upload.models import Document,Folder,File
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from upload.forms import DocumentForm,FolderForm,FileForm,SearchForm

import os
import random
import struct
import sys
from Crypto.Cipher import AES
import hashlib
import getpass
# password = 'bitch'
# password = getpass.getpass()

# from uploads.core.models import Document
# from uploads.core.forms import DocumentForm

def make_new_folder(request,form_id):
    parent = Folder.objects.filter(pk = form_id)
    # print(request.get_full_path())

    childforms = Folder.objects.filter(parentfolder = parent[0],author = request.user)
    childfiles = File.objects.filter(parentfolder = parent[0],author = request.user)
    if request.method == 'POST':
        # print('xyz' in request.POST)
        if 'foldersubmitbutton' in request.POST:
            form = FolderForm(request.POST, request.FILES)
            if form.is_valid():
                temp = form.save(commit = False)
                temp.author = request.user
                
                temp.parentfolder = parent[0]
                temp.save()

                return redirect(request.get_full_path())
            else:
                return render(request,'upload/error_page.html')
        elif 'filesubmitbutton' in request.POST:
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                temp = form.save(commit = False)
                temp.author = request.user
                
                temp.parentfolder = parent[0]
                temp.save()
                # form.save()

                return redirect(request.get_full_path())
            else:
                return render(request,'upload/error_page.html')

    else:
        folderform = FolderForm()
        fileform = FileForm()
    return render(request, 'upload/make_new_folder.html', {
        'folderform': folderform , 'fileform': fileform, 'childfolders' : childforms , 'childfiles' : childfiles
    })



def rootfinder(request):
    root = Folder.objects.filter(parentfolder__isnull = True,author = request.user)
    if len(root) > 0:
        root = root[0]
        url =  str(root.pk) + "/"
        return redirect(url)
    else:
        root = Folder.objects.create(name = request.user.username, author = request.user)
        root.save()
        url =  str(root.pk) + "/"
        return redirect(url)



def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # print(request.POST['searchstr'])
            searchstr = request.POST['search']
            files = File.objects.filter(name__icontains=searchstr,author=request.user)

            return render(request, 'upload/file_list.html',{'files': files})
        else:
            return render(request,'upload/error_page.html')
    else:
        form = SearchForm()
    return render(request, 'upload/search.html', {
        'form': form
    })













def file_list(request):
    print(request.get_full_path())
    files = Document.objects.filter(author = request.user)
    for root, dirs, files in os.walk('media/new'):
        print(files[0])
    # files = Document.objects.all()
    # return render(request, 'upload/file_list.html', {'files': files})
    return render(request, 'upload/file_list.html',{'files': files})

# def uploading(request):
# 	des = request.POST['description']
# 	doc = request.POST['document']

# 	File.objects.create(description=des,document=doc)
# 	return render(request, 'upload/upload_form.html')


# def uploading(request):
# 	if request.method == 'POST' and request.FILES['myfile']:
# 		myfile = request.FILES['myfile']
# 		fs = FileSystemStorage()
# 		filename = fs.save(myfile.name, myfile)
# 		uploaded_file_url = fs.url(filename)
# 		return render(request, 'upload/upload_form.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'upload/upload_form.html')


def uploading(request):
    if request.method == 'POST':
        # print(request.POST['author'])
        # print(request.user.id)
        form = DocumentForm(request.POST, request.FILES)
        if int(request.POST['author']) == int(request.user.id):
            print("yasss")
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            # print("nooo")
            return render(request,'upload/error_page.html')
    else:
        form = DocumentForm()
    return render(request, 'upload/upload_form.html', {
        'form': form
    })


@csrf_exempt
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'upload/upload_form.html')
        else:
            return render(request, 'upload/file_list.html')
    else:
        return render(request, 'upload/file_list.html')