# from flask import Flask, request
# from flask_cors import CORS
import nltk
import re
import collections

# app = Flask(__name__)
# CORS(app)

# @app.route('/submit')

# def submit():
#     value = input("Ievadiet apstrādājamo tekstu: ")
#     normalized_text = normalize_text(value)
#     return f"Normalized text:\n{normalized_text}"

# TODO
# Katram tokenam pievienot vērtību.
# 2 veidi: 
# papildināt frequency funkciju {token}: {count}, {VERTIBA}
# jaunā funkcijā izveidot jaunu array {token}: {value}


def frequency(tokenObject):
    token_counts = collections.Counter(tokenObject)
    frequency_results = []
    for token, count in token_counts.items():
        frequency_results.append(f"{token}: {count}, {VERTIBA}")
    return frequency_results

def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    return tokens

# TODO
# Noņemt insignificant vārdus kā 'have', 'me', 'PM' etc.
# Maybe Latviski?

#def significator(text): 


def normalize_text(text):
    sentences = nltk.sent_tokenize(text)
    # Teksta vienības normalizēšana (lowercase)
    normalized_sentences = [sentence.lower() for sentence in sentences]
    # Teksta vienības normalizēšana (noņemt nenozīmīgus simbolus)
    normalized_sentences = [re.sub(r'\W+', ' ', sentence) for sentence in normalized_sentences]
    normalized_text = '\n'.join(normalized_sentences)
    return normalized_text

# MAIN FUNKCIJA

value = input("Ievadiet apstrādājamo tekstu: ")

normalizedText = normalize_text(value)
print(f"Normalizēts teksts:\n{normalizedText}")

normalizedText = significator(value)
print(f"Normalizēts teksts:\n{normalizedText}")

tokenizedText = tokenize_text(normalizedText)
print(f"Tokeni:\n{tokenizedText}")

frequentedText = frequency(tokenizedText)
print(f"Absolūtais biežums:\n{frequentedText}")

# if __name__ == '__main__':
#     app.run()