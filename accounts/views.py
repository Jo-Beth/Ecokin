from django.shortcuts import get_object_or_404, render, redirect
from .form import InscriptionForm
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Utilisateur
from django.contrib.auth.decorators import login_required
from signalements.models import Signalements
from django.http import HttpResponseForbidden
from notifications.models import Notifications
# Create your views here.

def inscription(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST, request.FILES)
         
        if form.is_valid():
            
            email= form.cleaned_data.get('email')
            
            if Utilisateur.objects.filter(email=email).exists():
                form.add_error('email', "Cet email est déjà utilisé.")
            
            else:
                
                
                utilisateur = form.save(commit=False)
                utilisateur.role = "citoyens"
                utilisateur.save()
                return redirect('login')
        else:
            
            print(form.errors)
            
          
    else:
        form = InscriptionForm()
        
        
    return render(request, "accounts/inscription.html", {"form": form})

def login_views(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
            
                return redirect("aller_a_mon_espace")
    else:
        form = AuthenticationForm()
        return render(request, "accounts/login.html", {"erreurs": "indentifiants incorrects"})
        
    return render(request, 'accounts/login.html', {"form": form})



def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    if request.user.role != "admis":
        return HttpResponseForbidden("Accès refusé.")
    
    return render(request, "accounts/liste_utilisateurs.html", {"utilisateurs": utilisateurs})

def supprimer_utilisateur(request, id):

    utilisateur = get_object_or_404(Utilisateur,id=id)
    utilisateur.delete()
    
    return redirect("liste_utilisateurs")


def dashboard_views(request):
    role = request.user.role
    if role == "citoyens":
        
        mes_signalements = Signalements.objects.filter(utilisateur=request.user)
        nombre_signalements = mes_signalements.count()
        contexte ={
            'user': request.user,
            'mes_signalements': mes_signalements,
            'nombre_signalements': nombre_signalements,
            'en_attente':mes_signalements.filter(etat='en_attente').count(),
            'en_cours': mes_signalements.filter(etat='en_cours').count(),
            'resolus': mes_signalements.filter(etat='resolu'),
            'notifications': Notifications.objects.user.filter(utilisateur=request.user).order_by("date_creation")[:5] 
    }
    
    
    return render(request, "dashboard/dashboard_Citoyens.html", contexte)

@login_required

def changer_role(request, pk):
    if request.user.role != "admin":
        return redirect("dashboard")
    utilisateur = get_object_or_404(Utilisateur, pk=pk)
    
    if request.method == "POST":
        utilisateur.role = request.POST.get("role")
        utilisateur.save()
        return redirect("dashboard")
    
    return render(request, "accounts/changer_role.html", {"utilisateur": utilisateur})

def logout_views(request):
    logout(request)
    return redirect("accueil")


    
    