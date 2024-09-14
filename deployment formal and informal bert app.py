import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Path to the saved model and tokenizer files
save_folder_path = 'C:/Users/Dell/Desktop/deployment bert/files'

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained(save_folder_path)

# Load the model
model = BertForSequenceClassification.from_pretrained(save_folder_path, from_tf=False, from_flax=False, trust_remote_code=True)

# Placeholder function for text conversion (replace with actual implementation)
# Placeholder function for text conversion (replace with actual implementation)
def convert_to_formal(text):
    informal_to_formal = {
        "u": "you", "brb": "be right back", "ttyl": "talk to you later", "omg": "oh my god", "idk": "I don't know",
        "btw": "by the way", "b4": "before", "gr8": "great", "l8r": "later", "thx": "thanks", "pls": "please",
        "ur": "your", "r": "are", "w/": "with", "cuz": "because", "msg": "message", "2nite": "tonight",
        "bday": "birthday", "bf": "boyfriend", "gf": "girlfriend", "lol": "laugh out loud", "np": "no problem",
        "thx": "thanks", "omw": "on my way", "fyi": "for your information", "asap": "as soon as possible",
        "bff": "best friend forever", "atm": "at the moment", "afaik": "as far as I know", "idc": "I don't care",
        "imo": "in my opinion", "ttys": "talk to you soon", "tmi": "too much information", "b4n": "bye for now",
        "cu": "see you", "hand": "have a nice day", "ilu": "I love you", "w/e": "whatever", "wbu": "what about you",
        "xoxo": "hugs and kisses", "afaik": "as far as I know", "bbl": "be back later", "bbs": "be back soon",
        "bc": "because", "gf": "girlfriend", "h8": "hate", "jk": "just kidding", "lmk": "let me know",
        "nvm": "never mind", "rofl": "rolling on the floor laughing", "smh": "shaking my head", "tbh": "to be honest",
        "ty": "thank you", "yw": "you're welcome", "cya": "see you", "ic": "I see", "k": "okay", "np": "no problem",
        "ttfn": "ta-ta for now", "gr8": "great", "hmu": "hit me up", "idc": "I don't care", "n/a": "not available",
        "qt": "cutie", "sup": "what's up", "bby": "baby", "g2g": "got to go", "w8": "wait", "l8": "late", "gr8": "great",
        "b4n": "bye for now", "tmi": "too much information", "tldr": "too long; didn't read", "np": "no problem",
        "fomo": "fear of missing out", "brb": "be right back", "ftw": "for the win", "smh": "shaking my head",
        "bday": "birthday", "bbl": "be back later", "fyi": "for your information", "jk": "just kidding", 
        "rofl": "rolling on the floor laughing", "tbh": "to be honest", "tyvm": "thank you very much", 
        "btw": "by the way", "cu": "see you", "dm": "direct message", "ez": "easy", "irl": "in real life", 
        "nvm": "never mind", "omw": "on my way", "ppl": "people", "rn": "right now", "smh": "shaking my head", 
        "tba": "to be announced", "tbc": "to be continued", "thx": "thanks", "wfh": "work from home", 
        "wyd": "what are you doing", "yolo": "you only live once", "gr8": "great", "imo": "in my opinion", 
        "irl": "in real life", "j/k": "just kidding", "l8": "late", "m8": "mate", "msg": "message", 
        "ppl": "people", "rly": "really", "srsly": "seriously", "tmrw": "tomorrow", "ttys": "talk to you soon", 
        "ur": "your", "w/": "with", "w/o": "without", "atm": "at the moment", "cya": "see you", "hand": "have a nice day",
        "ilu": "I love you", "thx": "thanks", "w/e": "whatever", "afaik": "as far as I know", "b4n": "bye for now",
        "brb": "be right back", "cu": "see you", "fyi": "for your information", "gr8": "great", "h8": "hate",
        "idc": "I don't care", "idk": "I don't know", "imo": "in my opinion", "j/k": "just kidding", "l8": "late",
        "m8": "mate", "msg": "message", "n/a": "not available", "np": "no problem", "ppl": "people", "r": "are",
        "rly": "really", "smh": "shaking my head", "srsly": "seriously", "thx": "thanks", "ttfn": "ta-ta for now",
        "ttyl": "talk to you later", "u": "you", "ur": "your", "w/": "with", "w/o": "without", "wyd": "what are you doing",
        "yolo": "you only live once", "btw": "by the way", "cu": "see you", "dm": "direct message", "ez": "easy",
        "irl": "in real life", "jk": "just kidding", "lmk": "let me know", "nvm": "never mind", "omw": "on my way",
        "ppl": "people", "rn": "right now", "smh": "shaking my head", "tbh": "to be honest", "thx": "thanks",
        "wfh": "work from home", "yolo": "you only live once", "gr8": "great", "imo": "in my opinion", "j/k": "just kidding",
        "l8": "late", "m8": "mate", "msg": "message", "np": "no problem", "ppl": "people", "r": "are", "rly": "really",
        "srsly": "seriously", "thx": "thanks", "w/": "with", "w/o": "without", "wyd": "what are you doing",
        "atm": "at the moment", "cya": "see you", "fyi": "for your information", "gr8": "great", "h8": "hate",
        "idc": "I don't care", "idk": "I don't know", "imo": "in my opinion", "j/k": "just kidding", "l8": "late",
        "m8": "mate", "msg": "message", "n/a": "not available", "np": "no problem", "ppl": "people", "r": "are",
        "rly": "really", "smh": "shaking my head", "srsly": "seriously", "thx": "thanks", "ttfn": "ta-ta for now",
        "ttyl": "talk to you later", "u": "you", "ur": "your", "w/": "with", "w/o": "without", "wyd": "what are you doing",
        "yolo": "you only live once", "brb": "be right back", "bbl": "be back later", "bbs": "be back soon",
        "cuz": "because", "gr8": "great", "ilu": "I love you", "np": "no problem",
        "btw": "by the way", "b4": "before", "gr8": "great", "l8r": "later", "thx": "thanks", "pls": "please",
        "ur": "your", "r": "are", "w/": "with", "cuz": "because", "msg": "message", "2nite": "tonight",
        "bday": "birthday", "bf": "boyfriend", "gf": "girlfriend", "lol": "laugh out loud", "np": "no problem",
        "omw": "on my way", "fyi": "for your information", "asap": "as soon as possible", "bff": "best friend forever",
        "atm": "at the moment", "afaik": "as far as I know", "idc": "I don't care", "imo": "in my opinion",
        "ttys": "talk to you soon", "tmi": "too much information", "b4n": "bye for now", "cu": "see you",
        "hand": "have a nice day", "ilu": "I love you", "w/e": "whatever", "wbu": "what about you", "xoxo": "hugs and kisses",
        "afaik": "as far as I know", "bbl": "be back later", "bbs": "be back soon", "bc": "because", "gf": "girlfriend",
        "h8": "hate", "jk": "just kidding", "lmk": "let me know", "nvm": "never mind", "rofl": "rolling on the floor laughing",
        "smh": "shaking my head", "tbh": "to be honest", "ty": "thank you", "yw": "you're welcome", "cya": "see you",
        "ic": "I see", "k": "okay", "np": "no problem", "ttfn": "ta-ta for now", "gr8": "great", "hmu": "hit me up",
        "idc": "I don't care", "n/a": "not available", "qt": "cutie", "sup": "what's up", "bby": "baby", "g2g": "got to go",
        "w8": "wait", "l8": "late", "gr8": "great", "b4n": "bye for now", "tmi": "too much information", "tldr": "too long; didn't read",
        "np": "no problem", "fomo": "fear of missing out", "brb": "be right back", "ftw": "for the win", "smh": "shaking my head",
        "bday": "birthday", "bbl": "be back later", "fyi": "for your information", "jk": "just kidding", "rofl": "rolling on the floor laughing",
        "tbh": "to be honest", "tyvm": "thank you very much", "btw": "by the way", "cu": "see you", "dm": "direct message",
        "ez": "easy", "irl": "in real life", "nvm": "never mind", "omw": "on my way", "ppl": "people", "rn": "right now",
        "smh": "shaking my head", "tba": "to be announced", "tbc": "to be continued", "thx": "thanks", "wfh": "work from home",
        "wyd": "what are you doing", "yolo": "you only live once", "gr8": "great", "imo": "in my opinion", "irl": "in real life",
        "j/k": "just kidding", "l8": "late", "m8": "mate", "msg": "message", "ppl": "people", "rly": "really", "srsly": "seriously",
        "tmrw": "tomorrow", "ttys": "talk to you soon", "ur": "your", "w/": "with", "w/o": "without", "atm": "at the moment",
        "cya": "see you", "hand": "have a nice day", "ilu": "I love you", "thx": "thanks", "w/e": "whatever", "afaik": "as far as I know",
        "b4n": "bye for now", "brb": "be right back", "cu": "see you", "fyi": "for your information", "gr8": "great", "h8": "hate",
        "idc": "I don't care", "idk": "I don't know", "imo": "in my opinion", "j/k": "just kidding", "l8": "late", "m8": "mate",
        "msg": "message", "n/a": "not available", "np": "no problem", "ppl": "people", "r": "are", "rly": "really", "smh": "shaking my head",
        "srsly": "seriously", "thx": "thanks", "ttfn": "ta-ta for now", "ttyl": "talk to you later", "u": "you", "ur": "your",
        "w/": "with", "w/o": "without", "wyd": "what are you doing", "yolo": "you only live once", "btw": "by the way", "cu": "see you",
        "dm": "direct message", "ez": "easy", "irl": "in real life", "jk": "just kidding", "lmk": "let me know", "nvm": "never mind",
        "omw": "on my way", "ppl": "people", "rn": "right now", "smh": "shaking my head", "tbh": "to be honest", "thx": "thanks",
        "wfh": "work from home", "yolo": "you only live once", "gr8": "great", "imo": "in my opinion", "j/k": "just kidding", "l8": "late",
        "m8": "mate", "msg": "message", "np": "no problem", "ppl": "people", "r": "are", "rly": "really", "srsly": "seriously",
        "thx": "thanks", "w/": "with", "w/o": "without", "wyd": "what are you doing", "atm": "at the moment", "cya": "see you",
        "fyi": "for your information", "gr8": "great", "h8": "hate", "idc": "I don't care", "idk": "I don't know", "imo": "in my opinion",
        "j/k": "just kidding", "l8": "late", "m8": "mate", "msg": "message", "n/a": "not available", "np": "no problem", "ppl": "people",
        "r": "are", "rly": "really", "smh": "shaking my head", "srsly": "seriously", "thx": "thanks", "ttfn": "ta-ta for now",
        "ttyl": "talk to you later", "u": "you", "ur": "your", "w/": "with", "w/o": "without", "wyd": "what are you doing",
        "yolo": "you only live once", "brb": "be right back", "bbl": "be back later", "bbs": "be back soon", "cuz": "because",
        "gr8": "great", "ilu": "I love you", "np": "no problem", "ttfn": "ta-ta for now", "cu": "see you", "fyi": "for your information",
        "h8": "hate", "idc": "I don't care", "idk": "I don't know", "imo": "in my opinion", "j/k": "just kidding", "l8": "late",
        "m8": "mate", "msg": "message", "n/a": "not available", "np": "no problem", "ppl": "people", "r": "are", "rly": "really",
        "smh": "shaking my head", "srsly": "seriously", "thx": "thanks", "ttfn": "ta-ta for now", "ttyl": "talk to you later",
        "u": "you", "ur": "your", "w/": "with", "w/o": "without", "wyd": "what are you doing",
        "atm": "at the moment", "cya": "see you", "fyi": "for your information", "gr8": "great",
        "h8": "hate", "idc": "I don't care", "idk": "I don't know", "imo": "in my opinion", "j/k": "just kidding",
        "l8": "late", "m8": "mate", "msg": "message", "n/a": "not available", "np": "no problem", "ppl": "people",
        "r": "are", "rly": "really", "smh": "shaking my head", "srsly": "seriously", "thx": "thanks", "ttfn": "ta-ta for now",
        "ttyl": "talk to you later", "u": "you", "ur": "your", "w/": "with", "w/o": "without", "wyd": "what are you doing",
        "yolo": "you only live once", "brb": "be right back", "bbl": "be back later", "bbs": "be back soon", "cuz": "because",
        "gr8": "great", "ilu": "I love you", "np": "no problem", "ttfn": "ta-ta for now", "cu": "see you", "fyi": "for your information",
        "h8": "hate", "idc": "I don't care", "idk": "I don't know", "imo": "in my opinion", "j/k": "just kidding", "l8": "late",
        "m8": "mate", "msg": "message", "n/a": "not available", "np": "no problem", "ppl": "people", "r": "are", "rly": "really",
        "smh": "shaking my head", "srsly": "seriously", "thx": "thanks", "ttfn": "ta-ta for now", "ttyl": "talk to you later",
        "u": "you", "ur": "your", "w/": "with", "w/o": "without", "wyd": "what are you doing", "yolo": "you only live once",
        "b4": "before", "b/c": "because", "b4n": "bye for now", "b/c": "because", "bff": "best friend forever",
        "c": "see", "dat": "that", "dunno": "don't know", "fave": "favorite", "gonna": "going to",
        "gotta": "got to", "kinda": "kind of", "let's": "let us", "luv": "love", "nuff": "enough",
        "sorta": "sort of", "thru": "through", "til": "until", "wanna": "want to", "wassup": "what is up",
        "ya": "you", "yup": "yes", "yep": "yes", "cos": "because", "cuz": "because", "cya": "see you",
        "gimme": "give me", "lemme": "let me", "wanna": "want to", "innit": "isn't it", "imma": "I am going to",
        "kinda": "kind of", "gotta": "got to", "wanna": "want to", "gonna": "going to", "wassup": "what is up",
        "ya": "you", "whassup": "what is up", "aint": "is not", "wont": "will not", "shud": "should",
        "gud": "good", "fr": "for real", "idk": "I don't know", "nvm": "never mind", "rn": "right now",
        "sth": "something", "abt": "about", "tho": "though", "def": "definitely", "thru": "through",
        "coz": "because", "pls": "please", "plz": "please", "ur": "your", "h8": "hate", "msg": "message",
        "nvm": "never mind", "tl;dr": "too long; didn't read", "afk": "away from keyboard", "aka": "also known as",
        "asap": "as soon as possible", "bbl": "be back later", "bff": "best friends forever", "brb": "be right back",
        "btw": "by the way", "cu": "see you", "fyi": "for your information", "gr8": "great", "h8": "hate",
        "idk": "I don't know", "imo": "in my opinion", "irl": "in real life", "jk": "just kidding", "l8r": "later",
        "lol": "laugh out loud", "np": "no problem", "omg": "oh my god", "omw": "on my way", "rofl": "rolling on the floor laughing",
        "smh": "shaking my head", "thx": "thanks", "ttyl": "talk to you later", "u": "you", "ur": "your", "w/": "with",
        "w/o": "without", "w8": "wait", "whassup": "what is up", "wtf": "what the heck", "wyd": "what are you doing",
        "ya": "you", "yolo": "you only live once", "zomg": "oh my god", "bf": "boyfriend", "gf": "girlfriend",
        "bff": "best friend forever", "brb": "be right back", "dm": "direct message", "ez": "easy", "irl": "in real life",
        "jk": "just kidding", "k": "okay", "l8": "late", "lmao": "laughing my ass off", "np": "no problem",
        "omg": "oh my god", "rofl": "rolling on the floor laughing", "smh": "shaking my head", "tbh": "to be honest",
        "ttyl": "talk to you later", "u": "you", "ur": "your", "w/": "with", "w/o": "without", "wyd": "what are you doing",
        "yolo": "you only live once", "abt": "about", "b/c": "because", "bc": "because", "b4": "before",
        "brb": "be right back", "btw": "by the way", "cya": "see you", "dm": "direct message", "ez": "easy",
        "gr8": "great", "h8": "hate", "idk": "I don't know", "imo": "in my opinion", "irl": "in real life",
        "jk": "just kidding", "k": "okay", "l8r": "later", "lmao": "laughing my ass off", "nvm": "never mind",
        "omg": "oh my god", "rofl": "rolling on the floor laughing", "smh": "shaking my head", "tbh": "to be honest",
        "ttyl": "talk to you later", "u": "you", "ur": "your", "w/": "with", "w/o": "without", "wyd": "what are you doing",
        "yolo": "you only live once", "abt": "about", "b/c": "because", "bc": "because", "b4": "before",
        "brb": "be right back", "btw": "by the way", "cya": "see you", "dm": "direct message", "ez": "easy",
        "gr8": "great", "h8": "hate", "idk": "I don't know", "imo": "in my opinion", "irl": "in real life",
        "jk": "just kidding", "k": "okay", "l8r": "later", "lmao": "laughing my ass off", "nvm": "never mind",
        "omg": "oh my god", "rofl": "rolling on the floor laughing", "smh": "shaking my head", "tbh": "to be honest",
        "ttyl": "talk to you later", "u": "you", "ur": "your", "w/": "with", "w/o": "without", "wyd": "what are you doing",
        "yolo": "you only live once", "abt": "about", "b/c": "because", "bc": "because", "b4": "before",
        "brb": "be right back", "btw": "by the way", "cya": "see you", "dm": "direct message", "ez": "easy",
        "gr8": "great", "h8": "hate", "idk": "I don't know"
}

    # Replace informal words with formal equivalents
    for informal, formal in informal_to_formal.items():
        text = text.replace(informal, formal)
    return text

# Function to predict and convert text
def predict_and_convert(text):
    # Tokenize the input text
    inputs = tokenizer(text, truncation=True, padding='max_length', max_length=128, return_tensors='pt')
    
    # Make a prediction
    outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=-1).item()
    
    # Get the predicted label
    label = model.config.id2label[prediction]
    
    # Calculate the probability
    probabilities = torch.softmax(logits, dim=1)
    probability = probabilities[0][prediction].item()
    
    # Convert informal text to formal if prediction is informal
    if label == 'informal':
        formal_text = convert_to_formal(text)
    else:
        formal_text = text
    
    return label, probability, formal_text

# Streamlit application
st.title("Text Formalizer")
st.write("Enter the text below to check if it's informal and convert it to formal text automatically.")

user_input = st.text_area("Enter your text here:")

if user_input:
    label, probability, formal_text = predict_and_convert(user_input)
    st.write(f"**Original text:** {user_input}")
    st.write(f"**Predicted label:** {label}")
    st.write(f"**Probability:** {probability:.2f}")
    st.write(f"**Formal text:** {formal_text}")
