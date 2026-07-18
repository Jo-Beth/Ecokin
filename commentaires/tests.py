from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from articles.models import Article
from .models import Commentaire


class CommentaireTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='commenter',
            email='commenter@example.com',
            password='secret1234',
            role='autorités',
        )
        self.article = Article.objects.create(
            titre='Guide test',
            contenu='Contenu test',
            auteur=self.user,
            est_publie=True,
        )

    def test_ajout_commentaire(self):
        self.client.login(username='commenter', password='secret1234')
        response = self.client.post(
            reverse('ajouter_commentaire', args=[self.article.pk]),
            {'contenu': 'Très utile'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Commentaire.objects.filter(contenu='Très utile').exists())
