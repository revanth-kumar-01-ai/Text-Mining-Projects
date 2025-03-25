import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from Word_Cloud_Generator_1.src.main import scrape_and_process_text
import string
import re
import spacy
import contractions
from unidecode import unidecode
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import subprocess
from nltk.tokenize import word_tokenize 
from nltk.util import ngrams
from collections import Counter

def normalize_text(text):
    text = contractions.fix(text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = unidecode(text)
    return text

def preprocessingTextData(textData):
    sentences = sent_tokenize(textData)
    lower_sentences = [sentence.lower() for sentence in sentences]
    correct_sentences = [str(TextBlob(sentence).correct()) for sentence in lower_sentences]
    punctuation_free_sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in correct_sentences]
    
    stop_words = set(ENGLISH_STOP_WORDS)
    filtered_sentences = [" ".join([word for word in sentence.split() if word not in stop_words]) for sentence in punctuation_free_sentences]

    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
        nlp = spacy.load("en_core_web_sm")

    normalized_sentences = [normalize_text(sentence) for sentence in filtered_sentences]
    return normalized_sentences

def uniTokenization(textData):
    joined_text = " ".join(textData)
    tokenize = word_tokenize(joined_text)
    return tokenize

def biGramTokenization(textData):
    bigrams = list(ngrams(textData, 2))
    bigram_phrases = [" ".join(bigram) for bigram in bigrams]
    bigram_freq = Counter(bigram_phrases)
    return bigram_freq

def singleGramVisual(tokens):
    if tokens:
        text_for_wordcloud = " ".join(tokens)
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_for_wordcloud)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("No unigram tokens available for visualization.")

def biGramVisual(tokens):
    if tokens:
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(tokens)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("No bigram tokens available for visualization.")

st.session_state.setdefault("submitted", False)

st.title("BBC Articles Web Scraper & Word Cloud Generator")

url = st.text_input("Enter the article URL:")

if st.button("Submit"):
    if url:
        st.session_state.submitted = True
        st.write("Fetching content from:", url)

        single_tokens, bigram_tokens = scrape_and_process_text(url)

        if single_tokens and bigram_tokens:
            st.write("Tokenization successful! Generating Word Cloud...")
            singleGramVisual(single_tokens)
            biGramVisual(bigram_tokens)
        else:
            st.error("Failed to retrieve tokens. Please check the URL.")
    else:
        st.warning("Please enter a valid URL before submitting!")

if not st.session_state.submitted:
    st.title("How to Use")
    st.image("Word_Cloud_Generator_1/howTouse/one.png", caption="Example Word Cloud 1", use_container_width=True)
    st.image("Word_Cloud_Generator_1/howTouse/two.png", caption="Example Word Cloud 1", use_container_width=True)
    st.image("Word_Cloud_Generator_1/howTouse/three.png", caption="Example Word Cloud 1", use_container_width=True)
    st.image("Word_Cloud_Generator_1/howTouse/four.png", caption="Example Word Cloud 1", use_container_width=True)
    st.image("Word_Cloud_Generator_1/howTouse/five.png", caption="Example Word Cloud 1", use_container_width=True)