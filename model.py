import google.generativeai as genai

# Set the API key
api_key = "AIzaSyCLRJ7-se7XyyaPKVagqbZW9-mlTdRmHqE"
genai.configure(api_key=api_key)

# Define the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

# Create and configure the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

def classify_emotion(text):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(f"Classify the emotion of the following text: '{text}'")
    return response.text

def correct_grammar(text):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(f"Correct the grammar of the following text: '{text}'")
    return response.text

def identify_filler_words(text):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(f"Identify the filler words in the following text: '{text}'")
    return response.text

def identify_and_convert_formality(text):
    chat_session = model.start_chat(history=[])
    identification_response = chat_session.send_message(f"Is the following text formal or informal? '{text}'")
    formality = identification_response.text.strip().lower()
    if "informal" in formality:
        conversion_response = chat_session.send_message(f"Convert the following informal text to formal: '{text}'")
        formal_text = conversion_response.text
        return f"Original (Informal): {text}\nConverted (Formal): {formal_text}"
    else:
        return f"The text is already formal: {text}"

def identify_sentiment(text):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(f"Identify if the sentiment of the following text is positive or negative: '{text}'")
    return response.text
