import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

from data_preparation import clean_text
from load_data import (reverse_target_word_index, target_word_index,
                       x_tokenizer, y_tokenizer)
from settings import end_token, max_summary_len, max_text_len, nlp, start_token


# creating summary of input sequence
def decode_sequence_for_basic_seq2seq_model(input_sequence, encoder_model, decoder_model):
    # Encode the input as state vectors.
    e_out, e_h, e_c = encoder_model.predict(input_sequence)

    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1, 1))

    # Populate the first word of target sequence with the start word.
    target_seq[0, 0] = target_word_index[start_token]

    stop_condition = False
    decoded_sentence = ''

    while not stop_condition:
        output_tokens, h, c = decoder_model.predict(
            [target_seq] + [e_out, e_h, e_c])

        # Sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_token = reverse_target_word_index[sampled_token_index]

        if sampled_token != end_token:
            decoded_sentence += ' ' + sampled_token

        # Exit condition: either hit max length or find stop word.
        if (sampled_token == end_token) or (len(decoded_sentence.split()) >= (max_summary_len-1)):
            stop_condition = True

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index

        # Update internal states
        e_h, e_c = h, c

    return decoded_sentence


# For predicting unseen data pass decode_sequence function for which you want to decode
def predict_text(text, decode_sequence, encoder_model, decoder_model):
    original_text = text
    text = clean_text([text])  # generator
    text_list = original_text.split()

    if len(text_list) <= max_text_len:
        text = ['_START_ ' + str(doc) + ' _END_' for doc in nlp.pipe(text,
                                                                     batch_size=5000, n_threads=-1)][0]
        text = f'{start_token} {text} {end_token}'

        seq = x_tokenizer.texts_to_sequences([' '.join(text_list)])
        padded = pad_sequences(seq, maxlen=max_text_len, padding='post')
        pred_summary = decode_sequence(padded.reshape(
            1, max_text_len), encoder_model, decoder_model)
        return pred_summary
    else:
        pred_summary = ''

        # breaking long texts to individual max_text_len texts and predicting on them
        while len(text_list) % max_text_len == 0:
            text_list.append('')

        lst_i = max_text_len
        for i in range(0, len(text_list), max_text_len):
            _text_list = original_text.split()[i:i+lst_i]
            _text = ' '.join(_text_list)
            # to remove spaces that were added to make len(text_list) % max_text_len == 0
            _text = ' '.join(_text.split())

            _text = clean_text([_text])  # generator
            _text = ['_START_ ' + str(doc) + ' _END_' for doc in nlp.pipe(
                _text, batch_size=5000, n_threads=-1)][0]
            _text = f'{start_token} {_text} {end_token}'
            # print(_text, '\n')

            _seq = x_tokenizer.texts_to_sequences([_text])
            _padded = pad_sequences(_seq, maxlen=max_text_len, padding='post')
            _pred = decode_sequence(_padded.reshape(
                1, max_text_len), encoder_model, decoder_model)
            pred_summary += ' ' + ' '.join(_pred.split()[1:-2])
            pred_summary = ' '.join(pred_summary.split())

        return pred_summary
