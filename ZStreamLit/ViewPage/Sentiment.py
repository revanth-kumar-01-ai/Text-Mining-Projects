import streamlit as st
import re
import string
import joblib
import contractions
import pandas as pd
from unidecode import unidecode

from ZStreamLit.Preprocessing.sentiment import DataPreprocessing

st.header("Sentiment Prediction")  

# Text Input Field  
user_input = st.text_input("Enter your review:", "")  


if st.button("Predict"):
    data = DataPreprocessing(user_input)  
    st.write("Testing Output:", data)  
