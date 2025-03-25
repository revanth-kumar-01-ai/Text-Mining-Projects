from symspellpy import SymSpell
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import string
import re
import contractions
from unidecode import unidecode
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd 

# spelling correct  assets 
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

sym_spell.load_dictionary('ZStreamLit/assets/frequency_dictionary_en_82_765.txt', term_index=0, count_index=1)

def correct_spelling(text):
    corrected = sym_spell.lookup_compound(text, max_edit_distance=2)
    return corrected[0].term if corrected else text


# stop words assets
with open('ZStreamLit/assets/stop.txt', 'r', encoding = 'utf-8') as file:
    stopWords = file.readlines()

stopWords = [word.replace('\n', '') for word in stopWords]

# normalize text assets
def normalize_text(text):
    text = contractions.fix(text) 
    text = re.sub(r'\s+', ' ', text).strip() 
    text = unidecode(text)  
    return text

# load the count vectorizer assets
def split_into_words(i):
    return [word for word in i.split(" ")]

preprocessedBow = joblib.load('ZStreamLit/models/preprocessedBow')
model = joblib.load('ZStreamLit/models/sentiment.joblib')

def DataPreprocessing(textData):

    lowerConversion = textData.lower()

    spellingCorrection = correct_spelling(lowerConversion)

    punctual_removal = spellingCorrection.translate(str.maketrans('', '', string.punctuation+'\n'))
    
    stopWordsRemoval = " ".join([words for words in punctual_removal.split() if words not in stopWords])

    normalizeText = normalize_text(stopWordsRemoval)

    preprocessData  = preprocessedBow.transform([normalizeText])

    return model.predict(preprocessData)