from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('register/', views.inscription, name='inscription'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('changer_role/<int:pk>', views.changer_role, name='changer_role'),
    path('utilisateurs/', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('utilisateurs/supprimer/<int:id>/', views.supprimer_utilisateur, name='supprimer_utilisateur'),
    
]