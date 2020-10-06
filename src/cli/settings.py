import spacy

nlp = spacy.load('en', disable=['ner', 'parser'])
start_token = 'sostok'
end_token = 'eostok'
max_text_len = 80
max_summary_len = 15


# ================================
# Data
# ================================
# these files are avaiable at https://www.kaggle.com/akashsdas/text-summarization/output
# download these files and create a folder named data in this directory and the move the downloaded 
# files in the ./data folder without changing their names, if you change their name then you have 
# to change names here also for the respective ones

# tokenizers
X_TOKENIZER = './data/x_tokenizer'
Y_TOKENIZER = './data/y_tokenizer'

# ai model
AI_MODEL = './data/model.h5'

# inference models
ENCODER_MODEL = './data/encoder_model.h5'
DECODER_MODEL = './data/decoder_model.h5'


# ==========================
# If encounter this error
# OSError: [E050] Can't find model 'en'. It doesn't seem to be a shortcut
# link, a Python package or a valid path to a data directory.

# run this command on terminal => python -m spacy download en
