# from flask import Flask, request
# from flask_cors import CORS
import nltk
import re

# app = Flask(__name__)
# CORS(app)

# @app.route('/submit')

# def submit():
#     value = input("Ievadiet apstrādājamo tekstu: ")
#     normalized_text = normalize_text(value)
#     return f"Normalized text:\n{normalized_text}"

def normalize_text(text):
    sentences = nltk.sent_tokenize(text)
    # Teksta vienības normalizēšana (lowercase)
    normalized_sentences = [sentence.lower() for sentence in sentences]
    # Teksta vienības normalizēšana (noņemt nenozīmīgus simbolus)
    normalized_sentences = [re.sub(r'\W+', ' ', sentence) for sentence in normalized_sentences]
    normalized_text = '\n'.join(normalized_sentences)
    return normalized_text

value = input("Enter the text to be processed: ")
normalizedText = normalize_text(value)
print(f"Normalized text:\n{normalizedText}")

# if __name__ == '__main__':
#     app.run()