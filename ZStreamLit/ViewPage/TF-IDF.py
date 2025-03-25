import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

st.title("TF-IDF Vectorization")

# Sample documents
documents = [
    "Machine learning is amazing and powerful.",
    "Deep learning is a subset of machine learning.",
    "Artificial intelligence is the future of technology."
]

st.subheader("Input Documents")
st.write(documents)

# Step 1: TF-IDF Vectorization
st.subheader("1. Apply TF-IDF Vectorization")
code = """
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)
df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
"""
st.code(code, language="python")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)
df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

st.subheader("TF-IDF Matrix")
st.dataframe(df)
