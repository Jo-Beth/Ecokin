from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignalementsForm
from .models import Signalements
from notifications.models import Notifications
from .ai_utils import analyser_image

# Create your views here.

@login_required

def creer_signalements(request):
    prediction = None
    if request.method == 'POST':
        form = SignalementsForm(request.POST, request.FILES)
        if form.is_valid():
            photo = request.FILES.get('photo')
            if photo:
                prediction = analyser_image(photo)

            signalement = form.save(commit=False)
            signalement.utilisateur = request.user
            signalement.save()
            form = SignalementsForm()
            return render(request, 'signalements/creer_signalements.html', {'form': form, 'prediction': prediction, 'signalement_enregistre': True})
        
    else:
        form  = SignalementsForm()
        
    return render(request, 'signalements/creer_signalements.html', {'form': form, 'prediction': prediction})
@login_required
def liste_signalements(request):
    signalements= Signalements.objects.filter(utilisateur=request.user)
    return render (request, 'signalements/liste_signalements.html' ,{'signalements': signalements}
    ) 
    
@login_required
def liste_signalements_autorite(request):
    signalements = Signalements.objects.all()
    return render(request, "signalements/liste_autorite.html", {"signalements": signalements})
@login_required   
def detail_signalements(request,pk):
    signalements = get_object_or_404(Signalements, pk=pk)
    peut_modifier = request.user.peut_etre_modifier(signalements)
    peut_supprimer = request.user.peut_etre_supprimer(signalements)
    return render(request, "signalements/detail_signalements.html", {"signalements": signalements, "peut_modifier": peut_modifier, "peut_supprimer": peut_supprimer })
@login_required
def modifier_signalements(request, pk):
    signalements = get_object_or_404(Signalements, pk=pk)
    if  not request.user.peut_etre_modifier(signalements):
        return redirect('liste')
    
    if request.method == "POST":
        form = SignalementsForm(request.POST, request.FILES, instance=signalements)
        
        if form.is_valid():
            form.save()
            Notifications.objects.create(utilisateur=signalements.utilisateur, message=f"Votre'{signalements.titre}' a tété traité. ")
            return redirect("detail_signalements", pk=signalements.pk)
    
    else:
        form = SignalementsForm(instance=signalements)
    return render(request, "signalements/modifier_signalements.html", {"form":form, "signalements": signalements})
@login_required    
def supprimer_signalements(request, pk):
    signalements = get_object_or_404(Signalements, pk=pk)
    if not request.user.peut_etre_supprimer(signalements):  
        return redirect("detail_signalements", pk=pk)
    
    if request.method == "POST":
        signalements.delete()
    return render(request,"signalements/confirmer_suppression.html", {"signalements": signalements})
@login_required
def changer_statut(request, pk, nouveau_statut):
    signalements = get_object_or_404(Signalements, pk=pk)
    
    if request.method == "POST":
        nouveau_statut=request.POST.get("statut")
        signalements.statut = nouveau_statut
        signalements.save()
        Notifications.objects.create(utilisateur=signalements.utilisareur, message=f"Votre signalements'{signalements.titre}' a été mis à jourss" )
    
    return redirect("liste_autorite")
    
@login_required
def traiter_signalement(request, pk):
    if request.user.role != "autorités":
        
        return redirect("dashboard")
    
    signalements = get_object_or_404(Signalements, pk=pk)
    
    if request.method == "POST":
        nouveau_statut = request.POST.get("statut")
        signalements.statut = nouveau_statut
        signalements.save()
        Notifications.objects.create(utilisateur=signalements.utilisateur, message=f"le statut de votre signalement '{signalements.titre}' a été mis à jours :{signalements.get_statut_display()}.", lu=False)
        
        return redirect("dashboard")
    return render(request,"signalements/traiter.html", {"signalement": signalements})
           
@login_required                
def carte_signalements(request):
    statut = request.GET.get("etat")
    signalements = Signalements.objects.all().order_by('-date_creation')
    if statut:
        signalements = signalements.filter(statut=statut)

    return render(request, "signalements/carte_signalements.html", {
        "signalements": signalements,
        "statut": statut,
    })