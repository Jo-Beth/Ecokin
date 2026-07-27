from django.shortcuts import get_object_or_404, render, redirect
from .models import Notifications
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def notifications(request):
    liste_notifications = Notifications.objects.filter(utilisateur=request.user).order_by('date_creation')
    return render(request, 'notifications/notifications.html', {'notifications': liste_notifications})
@login_required
def lire_notification(request, pk):
    notification = get_object_or_404(Notifications, pk=pk, utilisateur=request.user)
    notification.lu = True
    notification.save()
    
    if notification.signalement:
        return redirect('detail_signalements', pk=notification.signalement.pk)
    return redirect('notifications')

@login_required
def tout_marquer_lu(request):
    Notifications.objects.filter(utilisateur=request.user, lu=False).update=True
    
    return redirect("notifications")