import tensorflow as tf 
import cv2
import numpy as np

# Charger le modèle
model = tf.keras.models.load_model('C:/Users/lenovo/Desktop/machine_learning_IA/converted_keras2/keras_model2.h5')
print("Modèle chargé avec succès")

# Ouvrir la webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la caméra.")
    exit()

# Variables pour stocker les chiffres et opérateurs
operand1 = ""
operand2 = ""
operator = None
result = None

# Étiquettes correspondant aux classes dans le modèle
labels = ['n0', 'n1', 'n2', 'n3', 'n4', 'n5', 'mult', 'egale', 'rien']

# Seuil pour considérer une prédiction valide
THRESHOLD = 0.7

while True:
    # Lire une image de la webcam
    ret, frame = cap.read()
    if not ret:
        print("Erreur lors de la lecture de l'image.")
        break

    # Prétraiter l'image pour la prédiction
    image_resized = cv2.resize(frame, (224, 224))
    image_normalized = image_resized.astype('float32') / 255.0
    image_input = np.expand_dims(image_normalized, axis=0)

    # Faire la prédiction
    predictions = model.predict(image_input)
    max_prob = np.max(predictions)
    predicted_class = np.argmax(predictions)

    # Vérifier si la prédiction est valide
    if max_prob < THRESHOLD:
        detected_label = "rien"
    else:
        detected_label = labels[predicted_class]

    # Afficher la prédiction brute et la classe détectée
    print(f"Prédiction brute : {predictions}")
    print(f"Classe détectée : {detected_label} (Probabilité : {max_prob:.2f})")

    # Gestion des chiffres et des opérateurs
    if detected_label in ['n0', 'n1', 'n2', 'n3', 'n4', 'n5']:
        digit = detected_label[1]  # Extraire le chiffre (ex. 'n1' -> '1')
        if operator is None:  # Construire le premier opérande
            if len(operand1) < 2:  # Limiter à deux chiffres
                operand1 += digit
        else:  # Construire le deuxième opérande
            if len(operand2) < 2:  # Limiter à deux chiffres
                operand2 += digit
    elif detected_label == 'mult':
        operator = '*'  # Détecter l'opérateur
    elif detected_label == 'egale' and operand1 and operand2:
        # Calculer le résultat lorsque 'egale' est détecté
        try:
            result = int(operand1) * int(operand2)
        except ValueError:
            result = "Erreur"
        print(f"Résultat : {result}")

        # Réinitialiser les variables pour une nouvelle opération
        operand1, operand2, operator = "", "", None

    # Afficher les informations sur l'image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'Operand1: {operand1}', (10, 30), font, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'Operator: {operator if operator else ""}', (10, 60), font, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'Operand2: {operand2}', (10, 90), font, 1, (0, 255, 0), 2)
    if result is not None:
        cv2.putText(frame, f'Result: {result}', (10, 120), font, 1, (0, 0, 255), 2)

    # Afficher l'image
    cv2.imshow('Webcam', frame)

    # Quitter si 'q' est pressé
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la webcam et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
