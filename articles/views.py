from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from categories.models import Category
from .forms import ArticleForm
from .models import Article


def liste_articles(request):
    """Affiche les ressources publiées et permet de les filtrer par type, acteur et catégorie."""
    articles = Article.objects.filter(est_publie=True)

    type_ressource = request.GET.get('type_ressource')
    acteur = request.GET.get('acteur')
    categorie = request.GET.get('categorie')

    if type_ressource:
        articles = articles.filter(type_ressource=type_ressource)
    if acteur:
        articles = articles.filter(acteur=acteur)
    if categorie:
        articles = articles.filter(categories__slug=categorie)

    categories = Category.objects.all()

    return render(request, 'articles/liste_articles.html', {
        'articles': articles,
        'type_ressource': type_ressource or '',
        'acteur': acteur or '',
        'categorie': categorie or '',
        'categories': categories,
    })


def detail_article(request, pk):
    """Affiche le détail d'une ressource publiée avec ses commentaires associés."""
    article = get_object_or_404(Article, pk=pk, est_publie=True)
    return render(request, 'articles/detail_article.html', {'article': article})


@login_required
def creer_article(request):
    """Permet à un utilisateur connecté de publier une nouvelle ressource."""
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.save()
            form.save_m2m()
            return redirect('detail_article', pk=article.pk)
    else:
        form = ArticleForm()

    return render(request, 'articles/creer_article.html', {'form': form})


@login_required
def gestion_ressources(request):
    """Espace de gestion personnel pour consulter ses ressources et catégories associées."""
    articles = Article.objects.filter(auteur=request.user).order_by('-date_creation')
    categories = Category.objects.all()

    return render(request, 'articles/gestion_ressources.html', {
        'articles': articles,
        'categories': categories,
    })
