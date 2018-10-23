from django.shortcuts import render
from django.utils import timezone
from upload.models import Document
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login

from django.core.files.storage import FileSystemStorage

# from uploads.core.models import Document
# from uploads.core.forms import DocumentForm



def file_list(request):
    # files = Document.objects.all()
    # return render(request, 'upload/file_list.html', {'files': files})
    return render(request, 'upload/file_list.html')

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
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload/upload_form.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload/upload_form.html')


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