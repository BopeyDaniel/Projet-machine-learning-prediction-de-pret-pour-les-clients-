🎓 Student Success Analytics : 2e Science A
📌 Présentation du Projet
Ce projet de Machine Learning est un système d'alerte précoce destiné à l'établissement scolaire. Son but est de prédire, dès le milieu de l'année, quels élèves risquent d'échouer afin de mettre en place un tutorat ciblé.

Au lieu d'attendre les résultats de fin d'année, l'IA analyse les notes du premier semestre pour anticiper les difficultés.

🎯 Objectif
Prédire la réussite ou l'échec final (seuil de 50%).

Identifier les facteurs clés de l'échec (notes, progression, âge).

Agir en générant une liste d'intervention prioritaire pour les professeurs.

📊 Fonctionnement du Système (6 Étapes)
Collecte : Importation du fichier dataset_info_2e_science_A.csv.

Préparation : Nettoyage des données et calcul de la progression de l'élève.

Visualisation : Création de graphiques pour comprendre la santé globale de la classe.

Intelligence Artificielle : Utilisation de l'algorithme Random Forest pour apprendre les profils d'élèves.

Évaluation : Test de précision du modèle (vérification de sa fiabilité).

Décision : Génération d'un graphique de risque et d'une liste d'élèves à convoquer.


📈 Résultats Attendus
Précision du modèle : Un score élevé (ex: >85%) indiquant que l'IA se trompe rarement.

Importance des facteurs : Un graphique montrant si l'examen ou la progression est le plus important.

Liste d'Alerte : Un tableau clair classant les élèves du plus risqué au moins risqué.

📋 Exemple de Sortie (Alerte)
Nom      Rebecca  |  Sarah    |   Daniel
Postnom  Mbayo    |  Mukendi   |  Kabongo
Risque   89%      |  72%       | 45%
d'Échec 🔴 Élevé | 🔴 Élevé  |  🟠 Modéré
Niveau  d'Urgence |  Urgent    |  Surveillance
