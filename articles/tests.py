from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Article


class ArticleViewsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='secret1234',
            role='autorités',
        )

    def test_liste_articles_affiche_uniquement_les_articles_publies(self):
        Article.objects.create(
            titre='Guide local',
            contenu='Contenu test',
            auteur=self.user,
            est_publie=True,
        )
        Article.objects.create(
            titre='Brouillon',
            contenu='Contenu test',
            auteur=self.user,
            est_publie=False,
        )

        response = self.client.get(reverse('liste_articles'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Guide local')
        self.assertNotContains(response, 'Brouillon')

    def test_creer_article_redirige_si_non_connecte(self):
        response = self.client.get(reverse('creer_article'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)
