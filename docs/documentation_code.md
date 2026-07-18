# Documentation technique du code source

## 1. Structure générale
Le projet Écokin est une application Django organisée en modules fonctionnels.

## 2. Applications principales
- accounts : gestion des utilisateurs et rôles.
- signalements : création et suivi des signalements environnementaux.
- articles : publication de ressources collaboratives.
- commentaires : échanges autour des ressources.
- categories : catégorisation des contenus.
- dashboard : interfaces adaptées par profil.
- notifications : messages et alertes d’activité.

## 3. Points d’entrée principaux
- Vue d’accueil : dashboard.views.accueil_view
- Tableau de bord : dashboard.views.basculer_vers_espace
- Création de signalement : signalements.views.creer_signalements
- Liste des articles : articles.views.liste_articles
- Détail d’un article : articles.views.detail_article
- Création d’un commentaire : commentaires.views.ajouter_commentaire

## 4. Intelligence artificielle
Le module signalements.ai_utils.analyser_image fournit un prototype d’analyse d’image basé sur la couleur dominante. Il permet de prédire une catégorie et une priorité approximative après le téléchargement d’une image.

## 5. Bonnes pratiques de maintenance
- Ajouter des docstrings aux nouvelles vues et modèles.
- Conserver une séparation claire entre logique métier et templates.
- Valider chaque évolution avec python manage.py check et les tests associés.
