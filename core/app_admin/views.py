from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from blog.models import Article
from blog.forms import ArticleForm
# Create your views here.
def borddash(request):
    return render(request,'dashbord.html')

def user_articles(request):
    if not request.user.is_authenticated:
        return redirect('home')

    list_articles=Article.objects.filter(user=request.user)
    return render(request,'my_article.html',{'list_articles':list_articles})

class AddArticle(CreateView):
    model=Article
    form_class=ArticleForm
    template_name="add-article.html"
    success_url="my_article"