
from django.contrib import admin
from django.urls import path

from articles import views

urlpatterns = [
    path('create/', views.articles_create, name= 'articles_create'),
    path('detail/', views.articles_detail, name= 'articles_detail'),
    path('list/<int:article_id>/', views.articles_list, name= 'articles_list'),
    path('update/', views.articles_update, name= 'articles_update'),
    path('delete/', views.articles_delete, name= 'articles_delete'),
]
