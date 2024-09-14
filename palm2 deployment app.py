import streamlit as st
from model import generate_text

# Streamlit app layout
st.title("NLP Model Interaction with Google PaLM API")

# Input box for API key
api_key = st.text_input("Enter your Google PaLM API key:", type="password")

if api_key:
    input_text = st.text_area("Enter text here:")

    if st.button("Emotion Classification"):
        prompt = f"""
        Classify the emotion expressed in the following sentence:

        "{input_text}"

        Provide the classification as one of the following emotions:
        - Happy
        - Sad
        - Angry
        - Fearful
        - Disgusted
        - Surprised
        - Neutral

        Sentence: "{input_text}"
        Emotion:
        """
        result = generate_text(api_key, prompt)
        st.write(result)

    if st.button("Correct Grammar"):
        prompt = f"""
        Check the following sentence for any grammar mistakes and provide a corrected version if there are any errors:

        Sentence: "{input_text}"

        Corrected Sentence:
        """
        result = generate_text(api_key, prompt)
        st.write(result)

    if st.button("Detect Filler Words"):
        prompt = f"""
        Identify and remove any filler words in the following sentence. Filler words include: um, uh, like, you know, etc.

        Sentence: "{input_text}"

        Corrected Sentence:
        """
        result = generate_text(api_key, prompt)
        st.write(result)

    if st.button("Convert to Formal"):
        prompt = f"""
        Identify if the following sentence is informal. If it is informal, convert it to a formal sentence.

        Sentence: "{input_text}"
        Formality:
        If informal, provide the formal version:
        """
        result = generate_text(api_key, prompt)
        st.write(result)

    if st.button("Sentiment Detection"):
        prompt = f"""
        Identify if the following sentence expresses a positive or negative sentiment. If it is negative, provide a more positive version of the sentence.

        Sentence: "{input_text}"

        Sentiment:
        If negative, provide a positive version:
        """
        result = generate_text(api_key, prompt)
        st.write(result)
else:
    st.warning("Please enter your Google PaLM API key to access the model.")
