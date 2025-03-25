import streamlit as st
import string
import re
import contractions
from unidecode import unidecode
from nltk.tokenize import sent_tokenize
from textblob import TextBlob
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import spacy
from nltk.stem import PorterStemmer

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
stemmer = PorterStemmer()

# Raw text
txt = """
Once upon a time!!!, there were two FRIENDS.. They are, umm, living in a small vlllage near the river. 
One day, as they were walking.. on the road, they saw.. a big dark cloud in the sky! 
"oh no...! I think it's going to rain heavily," said one friend. 

The other replied, "Nahh! don’t worry, bro. It's just a cloudd. Let's keep walking". 

Suddenly, a strong wind started blowingg! The trees began to shake, and the leaves flew everywhere. 
The friends rushed to find shelter near an old, abandoned hut. "See? I told you!" - the first friend exclaimed. 

After a few minutes, the rain poured down heavilly. They had nowhere else to go, so they sat under the hut waitingg...
"""

st.title("Text Cleaning Steps")

st.subheader("Cleaning Text")
st.write(txt)

# Step 1: Sentence Tokenization
st.subheader("1. Sentence Tokenization")
code1 = """
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(txt)
"""
st.code(code1, language="python")
sentences = sent_tokenize(txt)
st.write(sentences[:5])

# Step 2: Lowercase Conversion
st.subheader("2. Lowercase Conversion")
code2 = """
lower_sentences = [sentence.lower() for sentence in sentences]
"""
st.code(code2, language="python")
lower_sentences = [sentence.lower() for sentence in sentences]
st.write(lower_sentences[:5])

# Step 3: Spelling Correction
st.subheader("3. Spelling Correction")
code3 = """
from textblob import TextBlob
correct_sentences = [str(TextBlob(sentence).correct()) for sentence in lower_sentences]
"""
st.code(code3, language="python")
correct_sentences = [str(TextBlob(sentence).correct()) for sentence in lower_sentences]
st.write(correct_sentences[:5])

# Step 4: Punctuation Removal
st.subheader("4. Punctuation Removal")
code4 = """
import string 
punctuation_free_sentences = [sentence.translate(str.maketrans('', '', string.punctuation+'\n')) for sentence in correct_sentences]
"""
st.code(code4, language="python")
punctuation_free_sentences = [sentence.translate(str.maketrans('', '', string.punctuation+'\n')) for sentence in correct_sentences]
st.write(punctuation_free_sentences[:5])

# Step 5: Stop Words Removal
st.subheader("5. Stop Words Removal")
code5 = """
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stop_words = list(ENGLISH_STOP_WORDS)
filter_sentences = [" ".join([word for word in sentence.split() if word not in stop_words]) for sentence in punctuation_free_sentences]
"""
st.code(code5, language="python")
stop_words = list(ENGLISH_STOP_WORDS)
filter_sentences = [" ".join([word for word in sentence.split() if word not in stop_words]) for sentence in punctuation_free_sentences]
st.write(filter_sentences[:5])

# Step 6: Stemming
st.subheader("6. Stemming")
code6 = """
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemming_sentences = [" ".join([stemmer.stem(word) for word in sentence.split()]) for sentence in filter_sentences]
"""
st.code(code6, language="python")
stemming_sentences = [" ".join([stemmer.stem(word) for word in sentence.split()]) for sentence in filter_sentences]
st.write(stemming_sentences[:5])

# Step 7: Text Normalization
st.subheader("7. Text Normalization")
code7 = """
import contractions 
import re 
from unidecode import unidecode

def normalize_text(text):
    text = contractions.fix(text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = unidecode(text)
    return text

normalized_sentences = [normalize_text(sentence) for sentence in stemming_sentences]
"""

def normalize_text(text):
    text = contractions.fix(text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = unidecode(text)
    return text

st.code(code7, language="python")
normalized_sentences = [normalize_text(sentence) for sentence in stemming_sentences]
st.write(normalized_sentences[:5])

st.subheader("Final Cleaned Text")
st.write(" ".join(normalized_sentences))
