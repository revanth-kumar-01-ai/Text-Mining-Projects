import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from src.main import scrape_and_process_text

# Function to generate and display unigram word cloud
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

# Function to generate and display bigram word cloud
def biGramVisual(tokens):
    if tokens:
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(tokens)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("No bigram tokens available for visualization.")

# Ensure session state variable exists
st.session_state.setdefault("submitted", False)

# Streamlit App UI
st.title("BBC Articles Web Scraper & Word Cloud Generator")

# Input field for URL
url = st.text_input("Enter the article URL:")

# Submit button
if st.button("Submit"):
    if url:
        st.session_state.submitted = True  # Mark submission as done
        st.write("Fetching content from:", url)

        # Scrape and process text
        single_tokens, bigram_tokens = scrape_and_process_text(url)

        if single_tokens and bigram_tokens:
            st.write("Tokenization successful! Generating Word Cloud...")
            singleGramVisual(single_tokens)
            biGramVisual(bigram_tokens)
        else:
            st.error("Failed to retrieve tokens. Please check the URL.")
    else:
        st.warning("Please enter a valid URL before submitting!")

# Display "How to Use" section only if submission has NOT occurred
if not st.session_state.submitted:
    st.title("How to Use")
    st.image("../word_cloud_project/howTouse/one.png", caption="Example Word Cloud 1", use_container_width=True)
    st.image("../word_cloud_project/howTouse/two.png", caption="Example Word Cloud 1", use_container_width=True)
    st.image("../word_cloud_project/howTouse/three.png", caption="Example Word Cloud 1", use_container_width=True)
    st.image("../word_cloud_project/howTouse/four.png", caption="Example Word Cloud 1", use_container_width=True)
    st.image("../word_cloud_project/howTouse/five.png", caption="Example Word Cloud 1", use_container_width=True)
   
 



