from django.shortcuts import render, redirect
from django.utils import timezone
from upload.models import Folder,File
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from upload.forms import FolderForm,FileForm,SearchForm


def make_new_folder(request,form_id):
    parent = Folder.objects.filter(pk = form_id)

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


def filedelete(request,file_id):
    f = File.objects.get(pk = file_id)
    t = f.parentfolder.pk
    f.delete()
    return redirect("/upload/newfolder/"+str(t)+"/")

def folderdelete(request,folder_id):
    f = Folder.objects.get(pk = folder_id)
    t = f.parentfolder.pk
    f.delete()
    return redirect("/upload/newfolder/"+str(t)+"/")


def file_list(request):
    print(request.get_full_path())
    files = Document.objects.filter(author = request.user)
    for root, dirs, files in os.walk('media/new'):
        print(files[0])
    return render(request, 'upload/file_list.html',{'files': files})


# @csrf_exempt
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             # Redirect to a success page.
#             return render(request, 'upload/upload_form.html')
#         else:
#             return render(request, 'upload/file_list.html')
#     else:
#         return render(request, 'upload/file_list.html')