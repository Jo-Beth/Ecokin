from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .ai_utils import analyser_image


class AIAnalysisTests(TestCase):
    def test_analyser_image_detecte_un_type_simple(self):
        image_bytes = BytesIO()
        from PIL import Image

        image = Image.new('RGB', (200, 200), color=(0, 120, 255))
        image.save(image_bytes, format='PNG')
        image_bytes.seek(0)

        uploaded = SimpleUploadedFile('eau.png', image_bytes.read(), content_type='image/png')
        result = analyser_image(uploaded)

        self.assertEqual(result['categorie'], 'eau')
        self.assertIn(result['priorite'], {'moyenne', 'haute'})
