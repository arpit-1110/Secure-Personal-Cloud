from django.shortcuts import render
from upload.models import Folder
from upload.forms import FolderForm,SearchForm,FileForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def abc(request):
	print(request.user)
	Folder.objects.create(name = 'abc')
	return JsonResponse({'a' : 1},safe=False)

def rootfinder(request):

	root = Folder.objects.filter(parentfolder__isnull = True,author = request.user)
	if len(root) > 0:
		root = root[0]
	else:
		root = Folder.objects.create(name = request.user.username, author = request.user)
		root.save()
	return JsonResponse({'root' : root.pk},safe=False)

@csrf_exempt
def createfolder(request,parent_id):
	parent = Folder.objects.get(pk = parent_id)

	form = FolderForm(request.POST, request.FILES)
	if form.is_valid():
		temp = form.save(commit = False)
		temp.author = request.user
		temp.parentfolder = parent
		temp.save()
		key = temp.pk
		return JsonResponse({'key':key},safe = False)
	else:
		return JsonResponse({"error"},safe = False)

@csrf_exempt
def uploadfile(request,parent_id):
	parent = Folder.objects.get(pk = parent_id)

	form = FileForm(request.POST, request.FILES)
	if form.is_valid():
	    temp = form.save(commit = False)
	    temp.author = request.user
	    
	    temp.parentfolder = parent
	    temp.save()
	    key = temp.pk
	    return JsonResponse({'key':key},safe = False)
	else:
		# print("goes here")
		return JsonResponse({'error' : "error" },safe = False)


