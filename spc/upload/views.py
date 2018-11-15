from django.shortcuts import render, redirect
from django.utils import timezone
from upload.models import Document
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from upload.forms import DocumentForm

# from uploads.core.models import Document
# from uploads.core.forms import DocumentForm



def file_list(request):
    files = Document.objects.filter(author = request.user)
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
            # print("yasss")
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