# import necessary libraries 

import string
import re

import spacy
import contractions
from unidecode import unidecode
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def normalize_text(text):
    text = contractions.fix(text)
    text = re.sub('r\s+', ' ', text).strip()
    text = unidecode(text)
    return text

def preprocessingTextData(textData):
    
    # step one sentence boundary detection 
    sentences = sent_tokenize(textData)

    # step two Lower case conversion 
    lower_sentences = [sentence.lower() for sentence in sentences]

    # step three spelling correction 
    correct_sentences = [str(TextBlob(sentence).correct()) for sentence in lower_sentences]

    # step four Punctuation removal 
    punctuation_free_sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in correct_sentences]

    # Step five Stop Words Removal
    stop_words = list(ENGLISH_STOP_WORDS)
    filter_sentences = [" ".join([word for word in sentence.split() if word not in stop_words]) for sentence in punctuation_free_sentences]

    # Step six Lemmatization
    nlp = spacy.load('en_core_web_sm')
    lemmatized_sentences = [" ".join([token.lemma_ for token in nlp(sentence)]) for sentence in filter_sentences]

    #  Step 7: Text Normalization
    normalized_sentences  = [normalize_text(sentence) for sentence in lemmatized_sentences]

    return normalized_sentences