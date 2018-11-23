from django.shortcuts import render
from upload.models import Folder,File
from upload.forms import FolderForm,SearchForm,FileFormAPI
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
		# temp.save()
		# key = temp.pk
		lst = Folder.objects.filter(name = temp.name, parentfolder = parent, author = request.user)
		if len(lst) != 0:
			key = lst[0].pk
			return JsonResponse({'key':key,'status' : "no"},safe = False)
		else:
			temp.save()
			key = temp.pk
			return JsonResponse({'key':key,'status' : "yes"},safe = False)
		# return JsonResponse({'key':key},safe = False)
	else:
		return JsonResponse({"error"},safe = False)

@csrf_exempt
def uploadfile(request,parent_id):
	parent = Folder.objects.get(pk = parent_id)

	form = FileFormAPI(request.POST, request.FILES)
	if form.is_valid():
	    temp = form.save(commit = False)
	    temp.author = request.user
	    # temp.name = str(temp.file)
	    temp.parentfolder = parent
	    # temp.save()
	    key = temp.pk
	    # print("goes here")
	    lst = File.objects.filter(name = temp.name, parentfolder = parent, author = request.user)
	    # print(lst)
	    if len(lst) != 0:
	    	key = lst[0].pk
	    	lst[0].delete()
	    	temp.save()
	    	return JsonResponse({'key':key,'status' : "no"},safe = False)
	    else:
	    	temp.save()
	    	key = temp.pk
	    	return JsonResponse({'key':key,'status' : "yes"},safe = False)
	    # return JsonResponse({'key':key},safe = False)
	else:
		print("no here")
		return JsonResponse({'error' : "error" },safe = False)


@csrf_exempt
def filedownload(request,parent_id):
	parent = Folder.objects.get(pk = parent_id)
	files = File.objects.filter(parentfolder = parent,author = request.user)

	infolist = []

	for file in files:
		dicti = {}
		dicti['name'] = file.name
		dicti['file'] = str(file.file)
		dicti['md5sum'] = file.md5sum
		infolist.append(dicti)

	return JsonResponse({'info' : infolist},safe = False)

def folderlist(request,parent_id):
	parent = Folder.objects.get(pk = parent_id)
	folders = Folder.objects.filter(parentfolder = parent,author = request.user)

	infolist = []

	for folder in folders:
		dicti = {}
		dicti['name'] = folder.name
		dicti['id'] = folder.pk
		infolist.append(dicti)
	try:
		parent_id = parent.parentfolder.pk
	except:
		temp = Folder.objects.filter(parentfolder__isnull = True, author = request.user)
		parent_id = temp[0].pk

	return JsonResponse({'folderlist' : infolist,'parent' : parent_id},safe = False)


