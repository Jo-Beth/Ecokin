from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil_view, name='accueil'),
    path('tableau-de-bord/', views.dashboard_views, name='dashboard'),
    path('mon-espace/', views.basculer_vers_espace, name='aller_a_mon_espace'),
    path('espace_ong', views.espace_ong_view, name='espace_ong'),
    path('espace_admin', views.espace_admin_views, name='espace_admin'),
]
