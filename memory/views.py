from django.shortcuts import render
from django.urls import reverse  
# Create your views here.
from memory.models import Article

def hello(request):
	hello = 'Hello friend'
	return render(request, 'memory/hello.html', context={'name':hello})

def hello_model_list(request):
	list_of_article =  Article.objects.all()
	return render(request, 'memory/hello_model_list.html', {'list_of_article':list_of_article})

def hello_model_detail(request, pk):
	article = Article.objects.get(pk=pk)
	title = article.title
	body = article.body
	pub_date = article.pub_date
	context = {'title':title, 'body':body, 'pub_date':pub_date}
	return render(request, 'memory/hello_model_detail.html', context)

