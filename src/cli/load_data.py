import pickle

from tensorflow.keras.models import load_model

from settings import (AI_MODEL, DECODER_MODEL, ENCODER_MODEL, X_TOKENIZER,
                      Y_TOKENIZER)

with open(X_TOKENIZER, 'rb') as f:
    x_tokenizer = pickle.load(f)

with open(Y_TOKENIZER, 'rb') as f:
    y_tokenizer = pickle.load(f)

model = load_model(AI_MODEL)
encoder_model = load_model(ENCODER_MODEL)
decoder_model = load_model(DECODER_MODEL)

reverse_target_word_index = y_tokenizer.index_word
reverse_source_word_index = x_tokenizer.index_word
target_word_index = y_tokenizer.word_index
