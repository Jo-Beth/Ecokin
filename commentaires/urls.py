from django.urls import path

from . import views

urlpatterns = [
    path('article/<int:article_id>/commenter/', views.ajouter_commentaire, name='ajouter_commentaire'),
]
