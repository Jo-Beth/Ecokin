from django.urls import path
from . import views

urlpatterns = [
    path("lire/<int:pk>/", views.lire_notification, name="lire"), 
    path('notifications/', views.notifications, name="notifications")
]
