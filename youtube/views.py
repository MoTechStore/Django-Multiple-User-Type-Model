from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'home.html', {})
	
def about(request):
    return render(request, 'about.html', {})
    
def me(request):
	return render(request, 'me.html', {})


def moses(request):
    return render(request, 'moses.html', {})	


	