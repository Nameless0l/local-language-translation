from keras.models import Model
from keras.layers import Input, LSTM, Dense
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.utils import plot_model
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import sys
import pickle

# Charger les données
input_texts = []
target_texts = []
input_characters = set()
target_characters = set()

with open('eng-french.txt', 'r', encoding='utf-8') as f:
    rows = f.read().split('\n')
    
for row in rows[:50000]:
    if '\t' in row:
        input_text, target_text = row.split('\t')
        target_text = '\t' + target_text + '\n'
        input_texts.append(input_text.lower())
        target_texts.append(target_text.lower())
        input_characters.update(list(input_text.lower()))
        target_characters.update(list(target_text.lower()))
print(len(input_texts))


input_characters = sorted(list(input_characters))
target_characters = sorted(list(target_characters))
num_encoder_tokens = len(input_characters)
num_decoder_tokens = len(target_characters)
max_encoder_seq_length = max([len(txt) for txt in input_texts])
max_decoder_seq_length = max([len(txt) for txt in target_texts])

# Fonction pour tokenizer les caractères
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

# Fonction pour préparer les données
def prepare_data(input_texts, target_texts, input_char_dict, target_char_dict,
                 max_encoder_seq_length, max_decoder_seq_length):
    # Tokenizer les caractères pour les données d'entrée
    encoder_input_data = tokenize_characters(input_texts, input_char_dict, max_encoder_seq_length)
    
    # Tokenizer les caractères pour les données de sortie (inputs et targets)
    decoder_input_data = tokenize_characters(target_texts, target_char_dict, max_decoder_seq_length)
    # decoder_target_data = tokenize_characters(target_texts[1:], target_char_dict, max_decoder_seq_length)
    decoder_target_data = tokenize_characters(['\t'] + target_texts[1:], target_char_dict, max_decoder_seq_length)
    
    return encoder_input_data, decoder_input_data, decoder_target_data

encoder_input_data, decoder_input_data, decoder_target_data = prepare_data(input_texts, target_texts, 
                                                                             input_characters, target_characters,
                                                                             max_encoder_seq_length, max_decoder_seq_length)


# Définir le modèle
encoder_inputs = Input(shape=(None, num_encoder_tokens))
encoder_lstm = LSTM(256, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)
encoder_states = [state_h, state_c]

decoder_inputs = Input(shape=(None, num_decoder_tokens))
decoder_lstm = LSTM(256, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
decoder_dense = Dense(num_decoder_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

# Entraîner le modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history= model.fit([encoder_input_data, decoder_input_data],decoder_target_data, batch_size=64, epochs=200, validation_split=0.2)

model.save('translation_model.h5')
model.summary()


# Tracer la précision et la perte
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Précision du modèle')
plt.ylabel('Précision')
plt.xlabel('Époque')
plt.legend(['Entraînement', 'Validation'], loc='upper left')
plt.savefig('accuracy.png')

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Perte du modèle')
plt.ylabel('Perte')
plt.xlabel('Époque')
plt.legend(['Entraînement', 'Validation'], loc='upper left')
plt.savefig('loss.png')
# plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
# Graphe 2

# Enregistrer les graphes de statistiques
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

# Plot accuracy
plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('accuracy1.png')

# Plot loss
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('loss1.png')

with open('input_characters.pkl', 'wb') as f:
    pickle.dump(input_characters, f)
with open('target_characters.pkl', 'wb') as f:
    pickle.dump(target_characters, f)

print(max_encoder_seq_length ,max_decoder_seq_length ,num_decoder_tokens , max_decoder_seq_length)

