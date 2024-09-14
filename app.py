import streamlit as st
from model import classify_emotion, correct_grammar, identify_filler_words, identify_and_convert_formality, identify_sentiment

# Emotion emojis dictionary
emotion_emojis = {
    "Disheartening": "😔",
    "Worried": "😟",
    "Curious": "🤔",
    "Surprised": "😲",
    "Formal": "🧑‍💼",
    "Assertive": "💪",
    "Confident": "😎",
    "Appreciative": "🙏",
    "Concerned": "😟",
    "Informal": "😌",
    "Regretful": "😞",
    "Encouraging": "👍",
    "Egocentric": "🤨",
    "Joyful": "😊",
    "Optimistic": "😁",
    "Excited": "🤩"
}

# Streamlit app
st.markdown("<h1 style='text-align: center; color: #FF5733;'>🌟✨ Text Analysis Tool ✨🌟</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #33B5FF;'>Analyze your text with AI-powered features!</h3>", unsafe_allow_html=True)

# Input Section
st.markdown("### 📝 Enter your text below:")
input_text = st.text_area("", placeholder="Type your text here...", height=200)

# Add a horizontal line
st.markdown("---")

# Columns for buttons
col1, col2, col3 = st.columns(3)

# Emotion Classification
with col1:
    if st.button("🎭 Classify Emotion"):
        if input_text:
            emotion = classify_emotion(input_text)
            emotion_stripped = emotion.strip()
            emoji = emotion_emojis.get(emotion_stripped, "❓")
            st.markdown(f"<h4>Classified Emotion: {emotion_stripped} {emoji}</h4>", unsafe_allow_html=True)

# Grammar Correction
with col2:
    if st.button("📝 Correct Grammar"):
        if input_text:
            corrected_text = correct_grammar(input_text)
            st.markdown("<h4>Corrected Text:</h4>", unsafe_allow_html=True)
            st.success(corrected_text)

# Filler Word Identification
with col3:
    if st.button("🔍 Identify Filler Words"):
        if input_text:
            filler_words = identify_filler_words(input_text)
            st.markdown("<h4>Filler Words:</h4>", unsafe_allow_html=True)
            st.warning(filler_words)

# More columns for other tasks
col4, col5 = st.columns(2)

# Formality Conversion
with col4:
    if st.button("💼 Convert to Formal"):
        if input_text:
            formal_text = identify_and_convert_formality(input_text)
            st.markdown("<h4>Formality Conversion:</h4>", unsafe_allow_html=True)
            st.info(formal_text)

# Sentiment Analysis
with col5:
    if st.button("😊 Analyze Sentiment"):
        if input_text:
            sentiment = identify_sentiment(input_text)
            emoji = "😊" if "positive" in sentiment.lower() else "😔"
            st.markdown(f"<h4>Sentiment: {sentiment} {emoji}</h4>", unsafe_allow_html=True)

# Footer Section
st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with 💻 and ❤️ by Sugumar</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>🔗 Connect with us!</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>📧 Email: ssugumar2001@gmail.com | 🌐 Website: www.sugumar.com</p>", unsafe_allow_html=True)
