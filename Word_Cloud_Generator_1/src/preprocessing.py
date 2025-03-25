# Import necessary libraries 
import string
import re
import spacy
import contractions
from unidecode import unidecode
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import subprocess

def normalize_text(text):
    text = contractions.fix(text)
    text = re.sub(r'\s+', ' ', text).strip()  # ✅ Fixed regex
    text = unidecode(text)
    return text

def preprocessingTextData(textData):
    # Step 1: Sentence Boundary Detection 
    sentences = sent_tokenize(textData)

    # Step 2: Lower Case Conversion 
    lower_sentences = [sentence.lower() for sentence in sentences]

    # Step 3: Spelling Correction 
    correct_sentences = [str(TextBlob(sentence).correct()) for sentence in lower_sentences]

    # Step 4: Punctuation Removal 
    punctuation_free_sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in correct_sentences]

    # Step 5: Stop Words Removal
    stop_words = set(ENGLISH_STOP_WORDS)  # ✅ Using set() for efficiency
    filtered_sentences = [" ".join([word for word in sentence.split() if word not in stop_words]) for sentence in punctuation_free_sentences]

    # # Step 6: Lemmatization
    # try:
    #     nlp = spacy.load("en_core_web_sm")
    # except OSError:
    #     subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    #     nlp = spacy.load("en_core_web_sm")

    # lemmatized_sentences = [" ".join([token.lemma_ for token in nlp(sentence)]) for sentence in filtered_sentences]

    # Step 7: Text Normalization
    normalized_sentences = [normalize_text(sentence) for sentence in filtered_sentences]

    return normalized_sentences
