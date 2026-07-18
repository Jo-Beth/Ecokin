from django.urls import path

from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('gestion/', views.gestion_ressources, name='gestion_ressources'),
    path('<int:pk>/', views.detail_article, name='detail_article'),
    path('nouveau/', views.creer_article, name='creer_article'),
   
]
