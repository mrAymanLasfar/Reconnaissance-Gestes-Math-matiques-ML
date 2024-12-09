
import tensorflow as tf
import cv2
import numpy as np
import time  # Importer le module time pour ajouter un délai

# Charger le modèle
model = tf.keras.models.load_model('C:/Users/lenovo/Desktop/machine_learning_IA/converted_keras/keras_model.h5')
print("Modèle chargé avec succès")

# Ouvrir la webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la caméra.")
    exit()

# Variables pour stocker les chiffres et opérateurs
operand1 = None
operand2 = None
operator = None
result = None

while True:
    # Lire une image de la webcam
    ret, frame = cap.read()

    if not ret:
        print("Erreur lors de la lecture de l'image.")
        break

    # Prétraiter l'image pour la prédiction
    image_resized = cv2.resize(frame, (224, 224))  # Adapter à la taille d'entrée du modèle
    image_normalized = image_resized.astype('float32') / 255.0  # Normaliser les pixels
    image_input = np.expand_dims(image_normalized, axis=0)  # Ajouter la dimension du batch

    # Faire la prédiction avec le modèle
    predictions = model.predict(image_input)
    
    # Récupérer l'indice de la classe prédite
    predicted_class = np.argmax(predictions)
    
    # Définir les étiquettes correspondant aux classes (1 à 5, +, -, =)
    labels = ['1', '2', '3', '4', '5', '+', '-', '=', 'autre']
    
    # Afficher la prédiction dans le terminal
    print(f"Prédiction brute: {predictions}")
    print(f"Classe prédite (index): {predicted_class}")
    print(f"Geste détecté : {labels[predicted_class]}")

    # Vérifier les opérandes et opérateurs
    print(f"Operand1: {operand1}, Operator: {operator}, Operand2: {operand2}")  # Debug

    # Effectuer les opérations mathématiques
    if labels[predicted_class] in ['1', '2', '3', '4', '5']:
        if operand1 is None:
            operand1 = int(labels[predicted_class])
        elif operator is None:
            operator = labels[predicted_class]
        elif operand2 is None:
            operand2 = int(labels[predicted_class])

    if operator and operand1 is not None and operand2 is not None and labels[predicted_class] == '=':
        # Calculer le résultat de l'opération mathématique
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2    #gesture_recognition

        # Afficher le résultat dans le terminal
        print(f"Résultat : {result}")

        # Réinitialiser les variables pour une nouvelle opération
        operand1, operand2, operator = None, None, None

    # Afficher la prédiction sur l'image (résultat)
    font = cv2.FONT_HERSHEY_SIMPLEX
    if result is not None:
        cv2.putText(frame, f'Result: {result}', (10, 50), font, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, f'Pred: {labels[predicted_class]}', (10, 30), font, 1, (0, 255, 0), 2)

    # Afficher l'image avec la prédiction
    cv2.imshow('Webcam', frame)

    # Faire une pause de 3 secondes entre chaque capture d'image
    time.sleep(3)

    # Sortir de la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la webcam et fermer la fenêtre
cap.release()
cv2.destroyAllWindows()
