from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
import re
import collections
import json
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['GET'])
def submit():
    #no projekta frontend tiek iegūts lietotāja ievadītais apkopojamais teksts un
    #teikumu skaits, cik vērtīgākos teikumus saglabāt apkopojumam
    text = request.args.get('text')
    importance_ratio = request.args.get('count')

    if text is None or importance_ratio is None:
        return jsonify(error='Missing argument (text, count) / Trūkst argumenti (text, count)'), 400

    #Izsauktas funkcijas: normalizācija -> tokenizācija -> tokenu biežumi -> tokenu vērtības -> teikumu vērtības
    normalizedText = normalize_and_remove_stopwords(text)
    tokenizedText = tokenize_text(normalizedText)
    frequentedText = frequency(tokenizedText)
    tokenValues = assign_token_values(frequentedText)
    sentenceWeights = calculate_sentence_weights(text, tokenValues, int(importance_ratio))

    response = jsonify(sentenceWeights)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

#funkcija piešķir katram žetonam vērtību atkarībā no tā sastapšanas reizēm:
#Jo biežāk sastapts tekstā, jo lielāka vērtība
def assign_token_values(token_list):
    token_counts = [token_count.split(': ') for token_count in token_list]
    token_counts = [(token, int(count)) for token, count in token_counts]
    total_count = sum(count for _, count in token_counts)
    token_values = {token: count / total_count for token, count in token_counts}
    return token_values

#saskaitīts katra tokena biežums
def frequency(tokenObject):
    token_counts = collections.Counter(tokenObject)
    frequency_results = []
    for token, count in token_counts.items():
        frequency_results.append(f"{token}: {count}")
    return frequency_results

def tokenize_text(text):
    tokens = nltk.word_tokenize(text)
    return tokens


#Funkcija normalizē tekstu un noņem nenozīmīgos vārdus (stop words), lai tālāk veiktu teksta tokenizāciju.
def normalize_and_remove_stopwords(text):
    stop_words = set(stopwords.words('english')) #NLTK bibliotēkas stop vārdi angļu valodā

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

#izmantojot funkcijā assign_token_values iegūtās žetonu vērtības, tiek saskaitīta katra teikuma vērtība
#un teksta apkopojumam izvēlēts count skaits teikumu.
def calculate_sentence_weights(text, token_values, count):

    #Sagatavojot vērtīgākos teikumus izvadei, tie tiek atgriezti sākuma stāvoklī (denormalizēti):
    def denormalize_sentence(sentence):
        # Pirmo burtu palielināšana
        sentence = sentence[:1].upper() + sentence[1:]
        # I palielināšana (angļu valodas nolūkos)
        sentence = re.sub(r'\b(i)\b', 'I', sentence)
        return sentence

    sentences = nltk.sent_tokenize(text)
    denormalized_sentences = [denormalize_sentence(sentence) for sentence in sentences]
    sentence_weights = []

    for sentence in denormalized_sentences:
        sentence_tokens = nltk.word_tokenize(sentence)
        weight_sum = sum(token_values.get(token.lower(), 0) for token in sentence_tokens)
        sentence_weights.append({"sentence": sentence, "weight": weight_sum})

    sorted_sentences = sorted(sentence_weights, key=lambda x: x['weight'], reverse=True)
    top_sentences = sorted_sentences[:count]

    return top_sentences
    
# Atkomentēt tālāko, ja gribiet redzēt starprezultātus jeb 'breakpoints'

# value = input("Ievadiet apstrādājamo tekstu: ")

# normalizedText = normalize_and_remove_stopwords(value)
# print(f"Normalizēts teksts:\n{normalizedText}")

# tokenizedText = tokenize_text(normalizedText)
# print(f"Tokeni:\n{tokenizedText}")

# frequentedText = frequency(tokenizedText)
# print(f"Absolūtais biežums:\n{frequentedText}")

# tokenValues = assign_token_values(frequentedText)
# print(f"Tokenu svaru vērtības: \n{tokenValues}")

# sentenceWeights = calculate_sentence_weights(value, tokenValues)
# json_data = json.dumps(sentenceWeights, indent=4, ensure_ascii=False)
# print(f"Svērtības svaru summa:\n{json_data}")

if __name__ == '__main__':
    app.run()