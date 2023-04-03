import tensorflow as tf
import numpy as np

# Charger le modèle
model_path = "s2s"
model = tf.keras.models.load_model(model_path)
max_seq_length =100
# Charger les index de mots source et cibles
source_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
target_tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
source_tokenizer.fit_on_texts([''])  # nécessaire pour éviter une erreur
target_tokenizer.fit_on_texts([''])  # nécessaire pour éviter une erreur
source_vocab_size = len(source_tokenizer.word_index) + 1
target_vocab_size = len(target_tokenizer.word_index) + 1

# Traduire une phrase source
source_text = "Hello world"
source_sequence = source_tokenizer.texts_to_sequences([source_text])
source_padded = tf.keras.preprocessing.sequence.pad_sequences(source_sequence, maxlen=max_seq_length, padding='post')
decoder_input = np.zeros((1, max_seq_length))
decoder_input[0, 0] = target_tokenizer.word_index['<start>']
for i in range(1, max_seq_length):
    outputs = model.predict([source_padded, decoder_input])
    predicted_id = np.argmax(outputs[0, i-1, :])
    if predicted_id == target_tokenizer.word_index['<end>']:
        break                                                                           
    decoder_input[0, i] = predicted_id
predicted_sequence = decoder_input[0, 1:i+1]
predicted_text = target_tokenizer.sequences_to_texts([predicted_sequence])[0]

print("Source : ", source_text)
print("Traduction : ", predicted_text)
