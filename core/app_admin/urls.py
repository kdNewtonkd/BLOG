from django.urls import path
from .import views
urlpatterns=[
    path('borddash',views.borddash,name='borddash'),
    path('my_article',views.user_articles,name='my_article'),
     path('ajouter-article',views.AddArticle.as_view(),name='ajouter-article'),
      path('update-article/<int:pk>',views.UpdateArticle.as_view(),name='update-article'),
       path('delete-article/<int:pk>',views.DeleteArticle.as_view(),name='delete-article')

]