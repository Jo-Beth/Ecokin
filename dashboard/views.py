from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Utilisateur
from notifications.models import Notifications
from signalements.models import Signalements
from signalements.ai_utils import analyser_image
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def accueil_view(request):
    """Vue d’accueil principale de la plateforme avec un message de bienvenue et les actions d’entrée."""
    form = AuthenticationForm()
    contexte = {
        'utilisateur': request.user,
        'form': form,
        'show_login_card': False,
        'afficher_hero': True,
    }

    return render(request, "dashboard/accueil.html", contexte)

@login_required
def dashboard_views(request):
    """Redirige vers le tableau de bord adapté selon le rôle de l’utilisateur."""
    if request.user.is_authenticated:
        return redirect('aller_a_mon_espace')

    form = AuthenticationForm()
    contexte = {
        'utilisateur': request.user,
        'form': form,
        'show_login_card': True,
    }

    return render(request, "dashboard/dashboard.html", contexte)


@login_required
def basculer_vers_espace(request):
    """Choisit le bon tableau de bord selon le rôle de l’utilisateur connecté."""
    if request.user.role == "citoyens":
        mes_signalements = Signalements.objects.filter(utilisateur=request.user)
        notifications = Notifications.objects.filter(utilisateur=request.user).order_by('date_creation')
        notifications_non_lues = notifications.filter(lu=False).count()
        contexte = {
            'total_signalements': mes_signalements.count(),
            'en_attente': mes_signalements.filter(statut='en_attente').count(),
            'en_cours': mes_signalements.filter(statut='en_cours').count(),
            'resolus': mes_signalements.filter(statut='resolu').count(),
            'rejetes': mes_signalements.filter(statut='rejete').count(),
            'notifications': notifications,
            'notifications_non_lues': notifications_non_lues,
        }
        return render(request, "dashboard/dashboard_Citoyens.html", contexte)

    elif request.user.role == "autorités":
        mes_signalements = Signalements.objects.all().order_by("date_creation")

        analyses = []
        for signalement in mes_signalements:
            if signalement.photo:
                try:
                    result = analyser_image(signalement.photo)
                    analyses.append({
                        'titre': signalement.titre,
                        'categorie': result['categorie'],
                        'priorite': result['priorite'],
                    })
                except Exception:
                    analyses.append({
                        'titre': signalement.titre,
                        'categorie': 'non disponible',
                        'priorite': 'moyenne',
                    })

        contexte = {
            'signalements': mes_signalements,
            'total_signalements': mes_signalements.count(),
            'en_attente': mes_signalements.filter(statut='en_attente').count(),
            'en_cours': mes_signalements.filter(statut='en_cours').count(),
            'resolus': mes_signalements.filter(statut='resolu').count(),
            'rejetes': mes_signalements.filter(statut='rejete').count(),
            'analyses_ia': analyses,
        }
        return render(request, "dashboard/dashboard_autorite.html", contexte)

    elif request.user.role == "ong":
        tous_les_signalements = Signalements.objects.all().order_by('date_creation')
        contexte = {
            'signalements': tous_les_signalements,
            'total_signalements': tous_les_signalements.count(),
            'en_attente': tous_les_signalements.filter(statut='en_attente').count(),
            'en_cours': tous_les_signalements.filter(statut='en_cours').count(),
            'resolus': tous_les_signalements.filter(statut='resolu').count(),
            'rejetes': tous_les_signalements.filter(statut='rejete').count(),
        }
        return render(request, "dashboard/dashboard_ong.html", contexte)

    elif request.user.role == "admin":
        utilisateurs = Utilisateur.objects.all()

        contexte = {
            'utilisateurs': utilisateurs,
            'nombre_utilisateurs': utilisateurs.count(),
            'nombre_citoyens': utilisateurs.filter(role="citoyens").count(),
            'nombre_autorités': utilisateurs.filter(role="autorités").count(),
            'nombre_ong': utilisateurs.filter(role="ong").count(),
        }

        return render(request, "dashboard/dashboard_admin.html", contexte)


@login_required
def espace_ong_view(request):
    tous_les_signalements = Signalements.objects.all().order_by('date_creation')
    return render(request, "dashboard/dashboard_ong.html", {"signalements": tous_les_signalements})


@login_required
def espace_admin_views(request):
    total_signalements = Signalements.objects.count()

    return render(request, 'dashboard/dashboard_admin.html', {'total_signalemetns': total_signalements})
@login_required
def signalements_suivis(request):
    signalements = Signalements.objects.exclude(statut="en_attente")
    
    contexte = {
        "signalements":signalements
    }
    
    return render(request, "dashboard/signalements_suivis.html", contexte)
    