from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from articles.models import Article
from .forms import CommentaireForm
from .models import Commentaire


@login_required
def ajouter_commentaire(request, article_id):
    article = get_object_or_404(Article, pk=article_id, est_publie=True)

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.article = article
            commentaire.auteur = request.user
            commentaire.save()
            return redirect('detail_article', pk=article.pk)
    else:
        form = CommentaireForm()

    return render(request, 'commentaires/ajouter_commentaire.html', {'form': form, 'article': article})
def espace_collaboration_views(request):
    commentaires_recents = Commentaire.objects.select_related('auteur', 'article').order_by('-pk') [:20]
    
    contexte = {
        'commentaires': commentaires_recents
    }
    
    return render(request, 'commentaires/espace_collaboration.html', contexte)