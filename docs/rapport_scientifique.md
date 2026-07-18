# Rapport scientifique du projet Écokin

## 1. Introduction
Écokin est une plateforme numérique de gestion de signalements environnementaux destinée à faciliter la collaboration entre citoyens, autorités, ONG, écoles et entreprises. L’objectif principal est de permettre la collecte, le suivi et l’analyse des incidents environnementaux à travers une interface web moderne et accessible.

## 2. Problématique
Les problèmes environnementaux sont souvent signalés de manière dispersée, avec peu de coordination entre les acteurs concernés. Les citoyens ont du mal à transmettre leurs observations de façon structurée, tandis que les autorités et les partenaires manquent souvent d’outils permettant d’analyser rapidement les signalements et de mobiliser des ressources adaptées.

## 3. Objectifs du projet
- Centraliser les signalements environnementaux.
- Faciliter la communication entre les acteurs de terrain.
- Proposer une plateforme collaborative pour les ressources et les bonnes pratiques.
- Intégrer une première logique d’intelligence artificielle pour l’analyse d’images et la prédiction de catégories et de priorités.

## 4. Méthodologie
Le projet a été développé avec une approche méthodologique itérative basée sur :
- l’analyse des besoins fonctionnels,
- la conception d’une architecture Django modulaire,
- l’implémentation progressive des modules principaux,
- la validation par tests et vérification du système.

## 5. Architecture du système
Le système est basé sur Django avec une architecture modulaire composée de plusieurs applications :
- accounts : gestion des utilisateurs et des rôles.
- signalements : création, suivi et traitement des signalements.
- articles : publication de ressources et contenus pédagogiques.
- commentaires : discussion collaborative autour des ressources.
- categories : gestion des catégories de contenu.
- dashboard : tableaux de bord par profil.
- notifications : alertes et suivi utilisateur.

Cette structure permet une séparation claire des responsabilités et facilite l’évolution du système.

## 6. Résultats obtenus
Le projet permet aujourd’hui :
- la création et le suivi de signalements environnementaux,
- la consultation de la carte des signalements,
- la publication de ressources et guides,
- la collaboration via un module de commentaires,
- l’intégration d’un prototype d’IA pour l’analyse d’image et la prédiction de catégorie/priorité.

## 7. Limites du projet
- L’intelligence artificielle actuelle est un prototype simple basé sur l’analyse couleur et non sur un modèle de deep learning réel.
- Le système n’intègre pas encore une authentification avancée ou une modération fine des commentaires.
- Certaines fonctionnalités de collaboration peuvent encore être améliorées avec des workflows plus avancés.

## 8. Conclusion
Écokin constitue une base solide pour une plateforme de gouvernance environnementale collaborative. Grâce à son architecture modulaire, il peut évoluer vers une solution plus robuste, plus intelligente et plus adaptée à l’usage institutionnel et citoyen.
