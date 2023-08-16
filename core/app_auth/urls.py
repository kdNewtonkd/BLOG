from django.urls import path
from .import views
urlpatterns=[
    path('login',views.login_blog,name='login-blog'),
    path('register',views.register,name='register-blog'),
    path('logout',views.deconnecter,name='logout-blog')


]