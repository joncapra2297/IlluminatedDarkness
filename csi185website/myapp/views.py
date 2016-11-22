from django.shortcuts import render

# Create your views here.

def all(request):
    lst=request.path_info.split('/')
    url=''
    while lst[len(lst)-1]!='':
    	url=lst.pop()+'/'+url
    return render(request,url)
