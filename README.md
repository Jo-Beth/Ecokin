# Ecokin

Plateforme numérique de signalement citoyen développée avec Django.

Ecokin permet aux habitants de Kinshasa de signaler facilement les problèmes de leur quartier : voirie, éclairage public, insalubrité, etc.

## 🚀 Technologies utilisées
- **Backend** : Python, Django
- **Frontend** : HTML5, CSS3, Bootstrap
- **Base de données** : SQLite
- **Autres** : Git, GitHub

## ⚙️ Installation

1. **Cloner le projet**
```bash
git clone https://github.com/Jo-Beth/Ecokin.git
cd Ecokin
2. *Créer et activer l'environnement virtuel*
python -m venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
3. *Installer les dépendances*
pip install -r requirements.txt
4. *Faire les migrations*
python manage.py migrate
5. *Lancer le serveur*
python manage.py runserver
Le site sera accessible sur : `http://127.0.0.1:8000/`

## 📌 Fonctionnalités
- Création de signalements avec photo et localisation
- Carte interactive des signalements
- Suivi du statut des signalements
- Interface responsive avec Bootstrap

## 👨‍💻 Auteur
Développé par *Jo-Beth*

### Ce que j'ai ajouté :
1.  `cd Ecokin` après le clone
2.  `venv` + `migrate` c'est obligatoire pour Django sinon ça ne lance pas
3.  Les emojis + sections pour que ça rende bien sur Github
4.  Lien du site local

Tu veux que je t'ajoute aussi une section "Captures d'écran" et "Contribution" ?
