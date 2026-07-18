# Rapport académique du projet Écokin

## 1. Introduction
Le développement de plateformes numériques orientées vers la gouvernance environnementale représente aujourd’hui une réponse pertinente aux défis liés à la collecte, au traitement et à la diffusion de l’information environnementale. Dans ce contexte, Écokin a été conçu comme une application web collaborative permettant de centraliser les signalements environnementaux, de favoriser la coordination entre les acteurs concernés et de promouvoir l’accès à des ressources utiles pour la sensibilisation et l’action collective.

## 2. Problématique
Les problèmes environnementaux sont souvent signalés de manière fragmentée et parfois sans suivi efficace. Les citoyens disposent rarement d’un canal clair pour rapporter un incident, tandis que les autorités, les ONG, les écoles et les entreprises n’ont pas toujours un espace commun pour collaborer, partager des connaissances et transformer rapidement les observations en actions concrètes. Ce constat justifie la nécessité d’un outil numérique adapté, accessible et interactif.

## 3. Objectifs de la recherche et du projet
L’objectif principal du projet est de concevoir une plateforme web capable de :
- faciliter la déclaration de signalements environnementaux,
- améliorer la coordination entre les différents acteurs,
- offrir une interface de suivi et d’analyse des données,
- valoriser la production de ressources partagées,
- intégrer une première logique d’intelligence artificielle pour assister à l’analyse d’images.

## 4. Méthodologie
Le projet a été mené selon une approche itérative basée sur le cycle de développement logiciel. La méthodologie retenue comprend plusieurs étapes :
1. Analyse des besoins fonctionnels et identification des acteurs.
2. Conception d’une architecture modulaire avec Django.
3. Développement progressif des modules principaux : utilisateurs, signalements, articles, commentaires, tableaux de bord et notifications.
4. Intégration d’un prototype d’intelligence artificielle pour l’analyse d’images.
5. Validation par vérification Django et tests unitaires ciblés.

## 5. Architecture technique
Le système repose sur le framework Django, choisi pour sa robustesse, sa modularité et sa capacité à gérer rapidement des applications web complètes. L’architecture est organisée autour de plusieurs applications indépendantes :
- accounts pour la gestion des comptes et rôles,
- signalements pour la collecte et le traitement des observations,
- articles pour la publication des ressources,
- commentaires pour la collaboration autour des ressources,
- categories pour la structuration des contenus,
- dashboard pour les interfaces de suivi,
- notifications pour l’alerte et la communication.

Cette structure favorise la maintenabilité, la réutilisation et l’évolutivité du système.

## 6. Résultats obtenus
Le prototype développé permet actuellement d’offrir une plateforme fonctionnelle et cohérente. Les principaux résultats sont les suivants :
- mise en place d’un système de signalement environnemental,
- visualisation des signalements via une interface intuitive,
- intégration d’un module de ressources et de collaboration,
- mise en œuvre d’un espace de commentaires autour des contenus,
- ajout d’un prototype d’IA permettant d’analyser une image et fournir une catégorie et une priorité estimées.

## 7. Discussion des résultats
Les résultats obtenus montrent que la plateforme répond à une partie importante des besoins initiaux. Elle propose un cadre numérique pragmatique pour transformer des observations locales en actions collectives. L’intégration de la logique d’IA apporte un complément utile en facilitant l’orientation et la priorisation des signalements, même si cette première version reste limitée à un prototype technique.

## 8. Limites du projet
Le présent projet présente toutefois certaines limites :
- l’IA intégrée est encore simple et repose sur une logique de classification basée sur la couleur dominante,
- la plateforme ne dispose pas encore d’un système avancé de modération ou d’authentification multi-niveau,
- certaines fonctionnalités de collaboration nécessitent encore une évolution vers des workflows plus sophistiqués,
- l’application reste à valider dans un contexte réel avec des utilisateurs finaux sur plusieurs cycles d’utilisation.

## 9. Conclusion
Écokin constitue une base solide pour un système de gouvernance environnementale numérique. Il démontre la possibilité de construire une plateforme collaborative, accessible et évolutive autour de la problématique du signalement environnemental. Les perspectives d’évolution sont nombreuses, notamment en intégrant des modèles d’intelligence artificielle plus avancés, des mécanismes d’analyse prédictive et des fonctionnalités de collaboration plus riches.
