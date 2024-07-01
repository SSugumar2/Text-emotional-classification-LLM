import streamlit as st
from model import classify_emotion, correct_grammar, identify_filler_words, identify_and_convert_formality, identify_sentiment

# Streamlit app
st.title("Text Analysis Tool")

input_text = st.text_area("Enter the text:")

if st.button("Classify Emotion"):
    if input_text:
        emotion = classify_emotion(input_text)
        st.write(f"Classified Emotion: {emotion}")

if st.button("Correct Grammar"):
    if input_text:
        corrected_text = correct_grammar(input_text)
        st.write(f"Corrected Text: {corrected_text}")

if st.button("Identify Filler Words"):
    if input_text:
        filler_words = identify_filler_words(input_text)
        st.write(f"Filler Words: {filler_words}")

if st.button("Convert to Formal"):
    if input_text:
        formal_text = identify_and_convert_formality(input_text)
        st.write(f"Formality Conversion: {formal_text}")

if st.button("Analyze Sentiment"):
    if input_text:
        sentiment = identify_sentiment(input_text)
        st.write(f"Sentiment: {sentiment}")
