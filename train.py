import tensorflow as tf

# Charger le modèle entraîné
model = tf.keras.models.load_model('translation_model.h5')

# Charger les tokenizers
import pickle
with open('input_tokenizer.pickle', 'rb') as handle:
    input_tokenizer = pickle.load(handle)
with open('target_tokenizer.pickle', 'rb') as handle:
    target_tokenizer = pickle.load(handle)

# Fonction pour traduire du texte
def translate(input_text):
    # Prétraitement du texte d'entrée
    input_sequence = input_tokenizer.texts_to_sequences([input_text])
    input_data = tf.keras.preprocessing.sequence.pad_sequences(input_sequence, maxlen=max_input_length)
    
    # Prédiction
    prediction = model.predict(input_data)
    predicted_sequence = [np.argmax(pred) for pred in prediction[0]]
    
    # Décodage de la séquence prédite
    predicted_text = target_tokenizer.sequences_to_texts([predicted_sequence])[0]
    
    return predicted_text

# Exemple d'utilisation
input_text = "Bonjour tout le monde"
translated_text = translate(input_text)
print(translated_text)