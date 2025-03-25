import streamlit as st

from ZStreamLit import config

st.set_page_config(page_title = config.PROJECT_NAME, layout = 'wide')

home = st.Page(
    page = "ZStreamLit/ViewPage/Home.py", 
    title = "Home", 
    icon = '🏠' 
)

WordCloud = st.Page(
    page = "ZStreamLit/ViewPage/WordCloud.py", 
    title = "BBC Word Cloud", 
    icon = "🌐"
)

TextPreprocessing = st.Page(
    page = "ZStreamLit/ViewPage/TextPreprocessing.py", 
    title = "Text preprocessing", 
    icon = '⚙️' 
)

TFFrequency = st.Page(
    page = "ZStreamLit/ViewPage/TF-IDF.py", 
    title = "TF-IDF", 
    icon = '🔍' 
)

sentimentPrediction = st.Page(
    page = "ZStreamLit/ViewPage/Sentiment.py", 
    title = "Sentiment", 
    icon = '😊' 
)

st.logo('ZStreamLit/assets/logo.png', size = 'large')

pg = st.navigation({
    config.PROJECT_NAME:[home, WordCloud, TextPreprocessing, TFFrequency, sentimentPrediction]
})

pg.run()