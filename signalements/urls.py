from django.urls import path
from .import views

urlpatterns = [
    path('creer', views.creer_signalements, name='creer'),
    path('liste', views.liste_signalements, name='liste'),
    path('autorite/', views.liste_signalements_autorite, name='liste_autorite'),
    path('<int:pk>/', views.detail_signalements, name='detail_signalements'),
    path('traiter/<int:pk>', views.traiter_signalement, name='traiter'),
    path('<int:pk>/modifier/', views.modifier_signalements, name='modifier_signalements'),
    path('<int:pk>/supprimer/', views.supprimer_signalements, name='supprimer_signalements'),
    path('changer-statut/<int:pk>', views.changer_statut, name='changer_statut'),
    path('carte/', views.carte_signalements, name='carte_signalements'),
]
