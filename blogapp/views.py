from django.shortcuts import render, HttpResponse, get_object_or_404
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
	post = get_object_or_404(Article, pk=id)
	first = Article.objects.first()
	last = Article.objects.last()
	context = {
		"post":post,
		"first":first,
		"last":last
	}
	return render(request, 'single.html', context)

def getTopic(request, name):
	return render(request, 'category.html')
