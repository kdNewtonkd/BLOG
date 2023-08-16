from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Article
from blog.forms import ArticleForm
# Create your views here.
def borddash(request):
    return render(request,'dashbord.html')
@login_required
def user_articles(request):
    #if not request.user.is_authenticated:
        #return redirect('login-blog')
    list_articles=Article.objects.filter(user=request.user)
    return render(request,'my_article.html',{'list_articles':list_articles})

class AddArticle(LoginRequiredMixin,CreateView):
    model=Article
    form_class=ArticleForm
    template_name="add-article.html"
    success_url="my_article"

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid (form)
    
class UpdateArticle(LoginRequiredMixin,UpdateView):
    model=Article
    form_class=ArticleForm
    template_name='app_admin/update-article.html' 
    success_url='/my_admin/my_article'

class DeleteArticle(DeleteView):
    model=Article
    success_url='/my_admin/my_article'