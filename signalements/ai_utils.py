from io import BytesIO

from PIL import Image


def analyser_image(uploaded_file):
    """Prototype local de reconnaissance d’image basé sur l’analyse de la couleur dominante."""
    img = Image.open(uploaded_file).convert('RGB')
    img = img.resize((100, 100))

    pixels = list(img.getdata())
    r = sum(p[0] for p in pixels) // len(pixels)
    g = sum(p[1] for p in pixels) // len(pixels)
    b = sum(p[2] for p in pixels) // len(pixels)

    if b > g + 40 and b > 140:
        categorie = 'eau'
        priorite = 'haute'
    elif r > 150 and g > 140 and b < 120:
        categorie = 'dechets'
        priorite = 'moyenne'
    elif r < 100 and g < 100 and b < 100:
        categorie = 'pollution'
        priorite = 'haute'
    else:
        categorie = 'autre'
        priorite = 'moyenne'

    return {
        'categorie': categorie,
        'priorite': priorite,
        'couleur': (r, g, b),
    }
