from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
def piano(request):
	return HttpResponse('<p>This is my piano app</p>') # the site is show this html <p>