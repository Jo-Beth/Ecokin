from django.urls import path
from . import views

urlpatterns = [
    path("lire/<int:pk>/", views.lire_notification, name="lire_notification"), 
    path('notifications/', views.notifications, name="notifications"),
    path("tout_marquer_lu/", views.tout_marquer_lu, name="tout_marquer_lu"),
]
