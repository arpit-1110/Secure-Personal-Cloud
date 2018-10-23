from django.shortcuts import render
from django.utils import timezone
from upload.models import File
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login



def file_list(request):
    # files = File.objects()
    # return render(request, 'upload/file_list.html', {'files': files})
    return render(request, 'upload/file_list.html')

def uploading(request):
	des = request.POST['description']
	doc = request.POST['document']

	File.objects.create(description=des,document=doc)
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