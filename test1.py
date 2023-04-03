from keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pickle

# Charger le modèle et les caractères d'entrée/sortie
model = load_model('s2s/translation_model.h5')
with open('s2s/input_characters.pkl', 'rb') as f:
    input_characters = pickle.load(f)
with open('s2s/target_characters.pkl', 'rb') as f:
    target_characters = pickle.load(f)

max_encoder_seq_length ,max_decoder_seq_length ,num_decoder_tokens , max_decoder_seq_length=16 ,59 ,67, 59
print(target_characters)

def tokenize_characters(texts, char_dict, max_seq_length):
    tokenized_data = []
    for text in texts:
        tokenized_seq = []
        for char in text:
            char_idx = char_dict.index(char)
            char_vector = [0] * len(char_dict)
            char_vector[char_idx] = 1
            tokenized_seq.append(char_vector)
        # Pad avec des zéros si la séquence est plus courte que max_seq_length
        if len(tokenized_seq) < max_seq_length:
            padding = [[0] * len(char_dict)] * (max_seq_length - len(tokenized_seq))
            tokenized_seq.extend(padding)
        tokenized_data.append(tokenized_seq)
    return np.array(tokenized_data)


# Fonction pour traduire un message
def translate(input_text):
    # Tokenizer le message en entrée
    encoder_input = tokenize_characters([input_text.lower()], input_characters, max_encoder_seq_length)
    # Prédire la séquence de sortie en utilisant le modèle de traduction
    decoder_input = np.zeros((len(encoder_input), max_decoder_seq_length, num_decoder_tokens))
    decoder_input[:, 0, target_characters.index('\t')] = 1
    for i in range(1, max_decoder_seq_length):
        output_tokens = model.predict([encoder_input, decoder_input])
        sampled_token_index = np.argmax(output_tokens[:, i-1, :], axis=-1)
        decoder_input[:, i, sampled_token_index] = 1
    # Convertir la séquence de sortie en texte
    decoded_sentence = ''
    for token_vec in decoder_input[0]:
        sampled_char_idx = np.argmax(token_vec)
        sampled_char = target_characters[sampled_char_idx]
        if sampled_char == '\n':
            break
        decoded_sentence += sampled_char
    return decoded_sentence

# Boucle principale du chatbot
while True:
    # Lire le message entrant
    input_text = input('Vous: ')
    # Traduire le message
    output_text = translate(input_text)
    # Afficher la réponse
    print('Chatbot:', output_text)