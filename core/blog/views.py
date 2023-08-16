from django.shortcuts import render
from .models import Article
def home (request):
	list_articles=Article.objects.all()
	context={"list_articles":list_articles}
	return render(request,"index.html",context)

    

def detail(request,id_article):
	article=Article.objects.get(id=id_article)
	category=article.category
	article_en_relation=Article.objects.filter(category=category)
	return render(request,"detail.html",{"article":article,"aer":article_en_relation})



def search(request):
	query=request.GET["article"]
	list_art=Article.objects.filter(title__contains=query)
	return render(request,"search.html",{"list":list_art})