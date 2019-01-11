from django.shortcuts import render, HttpResponse
from .models import Author, Category, Article

def index(request):
	post = Article.objects.all()
	context = {
		"post": post
	}
	return render(request, 'index.html', context)

def getauthor(request, name):
	return render(request, 'profile.html')

def getsingle(request, id):
	return render(request, 'single.html')

def getTopic(request, name):
	return render(request, 'category.html')
