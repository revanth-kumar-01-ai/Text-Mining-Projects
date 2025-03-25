import streamlit as st

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
code_txt = '"""\n' + txt + '\n"""'
st.code(code_txt, language="python")

# Step 1: Sentence Tokenization
st.subheader("1. Sentence Tokenization")
code1 = """
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(txt)
"""
st.code(code1, language="python")

# Step 2: Lowercase Conversion
st.subheader("2. Lowercase Conversion")
code2 = """
lower_sentences = [sentence.lower() for sentence in sentences]
"""
st.code(code2, language="python")

# Step 3: Spelling Correction
st.subheader("3. Spelling Correction")
code3 = """
from textblob import TextBlob
correct_sentences = [str(TextBlob(sentence).correct()) for sentence in lower_sentences]
"""
st.code(code3, language="python")

# Step 4: Punctuation Removal
st.subheader("4. Punctuation Removal")
code4 = """
import string 
punctuation_free_sentences = [sentence.translate(str.maketrans('', '', string.punctuation+'\n')) for sentence in correct_sentences]
"""
st.code(code4, language="python")

# Step 5: Stop Words Removal
st.subheader("5. Stop Words Removal")
code5 = """
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stop_words = list(ENGLISH_STOP_WORDS)
filter_sentences = [" ".join([word for word in sentence.split() if word not in stop_words]) for sentence in punctuation_free_sentences]
"""
st.code(code5, language="python")

# Step 6: Stemming
st.subheader("6. Stemming")
code6 = """
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemming_sentences = [" ".join([stemmer.stem(word) for word in sentence.split()]) for sentence in filter_sentences]
"""
st.code(code6, language="python")

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
st.code(code7, language="python")

st.subheader("Final Cleaned Text")
code_final = """
final_text = " ".join(normalized_sentences)
"""
st.code(code_final, language="python")
