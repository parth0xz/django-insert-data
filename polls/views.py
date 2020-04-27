from django.http import HttpResponse
from django.shortcuts import render
from .models import Parth
def index(request):
	context = { 'parth': Parth.objects.all() }
	if request.method == 'POST':
	 	parth=Parth()
	 	parth.name = request.POST.get('name')
	 	parth.surname = request.POST.get('surname')
	 	parth.title = request.POST.get('title')
	 	parth.save()
	return render(request, 'polls/home.html' , context)
def about(request):
	return render(request,'polls/about.html')
