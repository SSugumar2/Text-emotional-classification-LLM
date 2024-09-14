import streamlit as st
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch

# Path to the saved model and tokenizer files
save_folder_path = 'C:/Users/Dell/Desktop/deployment emotion_classification_roberta/files'

# Load the tokenizer
tokenizer = RobertaTokenizer.from_pretrained(save_folder_path)

# Load the model
model = RobertaForSequenceClassification.from_pretrained(save_folder_path, from_tf=False, from_flax=False, trust_remote_code=True)

# Define emotion labels
emotion_labels = {
    0: "Disheartening",
    1: "Worried",
    2: "Curious",
    3: "Surprised",
    4: "Formal",
    5: "Assertive",
    6: "Confident",
    7: "Appreciative",
    8: "Concerned",
    9: "Informal",
    10: "Regretful",
    11: "Encouraging",
    12: "Egocentric",
    13: "Joyful",
    14: "Optimistic",
    15: "Excited"
}

def predict_emotion(text):
    encoding = tokenizer(text, truncation=True, padding='max_length', return_tensors='pt', max_length=128)
    output = model(**encoding)
    predicted_label = torch.argmax(output.logits, dim=1).item()
    predicted_emotion = emotion_labels.get(predicted_label, "Unknown")
    return predicted_emotion

def main():
    st.title("Emotion Prediction App")
    input_text = st.text_area("Enter your text here:")
    if st.button("Predict"):
        emotion = predict_emotion(input_text)
        st.write("Predicted Emotion:", emotion)

if __name__ == "__main__":
    main()
