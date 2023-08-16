from django.urls import path
from .import views
urlpatterns=[
    path('borddash',views.borddash,name='borddash'),
    path('my_article',views.user_articles,name='my_article'),
     path('ajouter-article',views.AddArticle.as_view(),name='ajouter-article'),

]