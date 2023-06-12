# from flask import Flask, request
# from flask_cors import CORS
import nltk
import re
import collections
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

# app = Flask(__name__)
# CORS(app)

# @app.route('/submit')

# def submit():
#     value = input("Ievadiet apstrādājamo tekstu: ")
#     normalized_text = normalize_text(value)
#     return f"Normalized text:\n{normalized_text}"

def assign_token_values(token_list):
    token_counts = [token_count.split(': ') for token_count in token_list]
    token_counts = [(token, int(count)) for token, count in token_counts]
    total_count = sum(count for _, count in token_counts)
    token_values = {token: count / total_count for token, count in token_counts}
    return token_values


def frequency(tokenObject):
    token_counts = collections.Counter(tokenObject)
    frequency_results = []
    for token, count in token_counts.items():
        frequency_results.append(f"{token}: {count}")
    return frequency_results

def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    return tokens


def normalize_and_remove_stopwords(text):
    stop_words = set(stopwords.words('english')) #NLTK bibliotēkas stop vārdi

    def remove_stopwords(tokens):
        filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
        return filtered_tokens

    def normalize_sentence(sentence):
        sentence = sentence.lower()
        sentence = re.sub(r'\W+', ' ', sentence)
        return sentence

    sentences = nltk.sent_tokenize(text)
    normalized_sentences = [normalize_sentence(sentence) for sentence in sentences]
    normalized_tokens = [nltk.word_tokenize(sentence) for sentence in normalized_sentences]
    filtered_tokens = [remove_stopwords(tokens) for tokens in normalized_tokens]
    filtered_sentences = [' '.join(tokens) for tokens in filtered_tokens]
    normalized_text = '\n'.join(filtered_sentences)
    return normalized_text

# TODO
# Izveidot funkciju teikumu vērtības noteikšanai, izmantojot aprēķinātās tokenu vērtības

# MAIN FUNKCIJA

value = input("Ievadiet apstrādājamo tekstu: ")

normalizedText = normalize_and_remove_stopwords(value)
print(f"Normalizēts teksts:\n{normalizedText}")

tokenizedText = tokenize_text(normalizedText)
print(f"Tokeni:\n{tokenizedText}")

frequentedText = frequency(tokenizedText)
print(f"Absolūtais biežums:\n{frequentedText}")

tokenValues = assign_token_values(frequentedText)
print(f"Tokenu vērtības: \n{tokenValues}")

# if __name__ == '__main__':
#     app.run()