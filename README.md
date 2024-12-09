# Reconnaissance de Gestes Mathématiques avec Python

## Description
Ce projet permet de reconnaître des gestes de la main représentant des chiffres et des opérateurs mathématiques, afin de réaliser des opérations simples directement en utilisant les gestes d'une personne. Le projet repose sur l'utilisation de **Teachable Machine** pour la création du modèle de reconnaissance des gestes et de **TensorFlow** pour charger et exécuter ce modèle. La capture vidéo est gérée via **OpenCV**.

## Fonctionnalités
- **Reconnaissance de chiffres** de `0` à `5`.
- **Reconnaissance des opérateurs mathématiques** tels que `+`, `-`, `*`, et `=`.
- Calcul en temps réel de l'expression mathématique basée sur les gestes effectués.
- Interface en temps réel avec la webcam pour capturer les gestes de la main.

## Prérequis

### Logiciels nécessaires
- **Python 3.10** ou supérieur.
- **Teachable Machine** : utilisé pour entraîner le modèle de reconnaissance des gestes.
- **OpenCV** : bibliothèque pour capturer et traiter les images de la webcam.
- **TensorFlow** : pour utiliser le modèle d'apprentissage automatique.

### Bibliothèques Python requises
- `tensorflow==2.13`
- `opencv-python`
- `numpy`
- `pillow`

### Installation des dépendances
1. Clonez ce dépôt ou téléchargez le projet.
2. Créez un environnement virtuel Python :
   ```bash
   python -m venv env





## Activez l'environnement virtuel :
# Sous Windows :

env\Scripts\activate
# Sous macOS/Linux :

source env/bin/activate

# Installez les dépendances :

pip install tensorflow==2.13 opencv-python numpy pillow

# Comment utiliser
# Étapes pour lancer le programme
# Téléchargez le modèle : 
Le modèle de reconnaissance des gestes a été créé avec Teachable Machine. Téléchargez-le en suivant les instructions de Teachable Machine, ou utilisez le modèle inclus dans ce projet.

# Lancez l'application : 
Exécutez le fichier principal fichier1.py pour démarrer le programme de reconnaissance :


# python fichier1.py
Utilisez la webcam : Lorsque le programme est lancé, il active la webcam et commence à capturer les gestes. Faites des gestes pour afficher des chiffres (0 à 5) ou des opérateurs mathématiques (+, -, *). Faites le geste = pour signaler la fin de l'expression et obtenir le résultat du calcul.

# Affichage du résultat : Le programme affiche le résultat de l'opération directement à l'écran.

# Structure du projet
Le projet est composé de plusieurs fichiers principaux, chacun ayant un rôle précis dans le fonctionnement global du programme.

# fichier1.py - Fichier principal
Ce fichier contient le code pour :

Configurer et démarrer la webcam.
Charger le modèle de reconnaissance de gestes.
Détecter les gestes de la main (chiffres et opérateurs).
Calculer et afficher les résultats en temps réel.
Exemple de lancement :  python fichier1.py

# fichier2.py - Fonctions auxiliaires
Ce fichier contient des fonctions utilitaires pour :

Charger et prédire avec le modèle Teachable Machine.
Traiter les gestes détectés par la webcam.
Effectuer les calculs basés sur les gestes.
Exemple d'appel de fonction dans fichier1.py : import fichier2
 
# fichier2.predict_gesture(image)
Modèle Teachable Machine
Le modèle de reconnaissance des gestes a été créé sur Teachable Machine, où les classes suivantes ont été définies :

Chiffres : 0, 1, 2, 3, 4, 5.
Opérateurs : +, -, *, =. Le modèle est exporté en format TensorFlow et chargé dans l'application via TensorFlow.
Exemple de fonctionnement
# Reconnaissance des chiffres : 
Lorsque vous faites un geste représentant un chiffre (par exemple, 3), le modèle le reconnaît et l'affiche à l'écran. Exemple : Vous montrez le chiffre 3, et l'interface affiche "3".

# Reconnaissance des opérateurs : 
Lorsqu'un opérateur comme + est détecté, le programme le capture et l'affiche. Exemple : Vous faites le geste +, et l'interface affiche "+".

# Calcul de l'expression : 
Après avoir effectué les gestes représentant les chiffres et les opérateurs, faites le geste = pour que l'opération soit calculée. Le résultat s'affiche ensuite. Exemple : Après avoir fait 3 + 2 =, l'interface affiche "5".

# Limitations
Sensibilité aux conditions d'éclairage : Le modèle peut avoir des difficultés à reconnaître les gestes si l'éclairage est trop faible ou trop fort.

# Reconnaissance limitée : 
Le modèle est actuellement configuré pour reconnaître uniquement les chiffres de 0 à 5 et les opérateurs de base.

# Variabilité des gestes : 
Le modèle peut ne pas être précis si les gestes effectués diffèrent trop de ceux utilisés pendant l'entraînement.

Améliorations futures
Étendre la reconnaissance à des chiffres au-delà de 5.
Ajouter plus d'opérateurs mathématiques comme la division (/).
Améliorer la robustesse aux conditions d'éclairage et aux arrière-plans.
Ajouter une interface graphique pour rendre l'application plus conviviale.


## Auteur
Ayman Lasfar

Ce projet a été développé dans le cadre d'un apprentissage en data science et en machine learning, utilisant des outils modernes tels que Teachable Machine, TensorFlow, et OpenCV.


Cette version du `README.md` présente une structure complète, allant des étapes d'installation et de lancement à la description du projet, du modèle utilisé, ainsi que des exemples d'utilisation.










