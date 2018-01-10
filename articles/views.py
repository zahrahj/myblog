
from django.http import HttpResponse
from django.shortcuts import render
import random
from .models import Article

# this is my view page
# Create your views here.
def articles_create(request):
	return render(request,'home.html', {})

def articles_detail(request):
	object_lest = Article.objects.all()
	context = { 
	"title": "user's details",
	"name": request.user,
	"number": random.randint(1, 50),
	"articles":object_lest
	}

	return render(request, 'detail.html', context)

def articles_list(request, article_id):
	thing = Article.objects.get(id= article_id)

	context = { "thing" :thing 
	}
	
	return render(request, 'list.html', context)

def articles_update(request):
	return HttpResponse("<h1> Update </h1>")
def articles_delete(request):
	return HttpResponse("<h1> Delete </h1>")
