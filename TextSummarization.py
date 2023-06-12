from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit')
def submit():
    value = request.args.get('value')
    return f"I have submitted: {value}"

if __name__ == '__main__':
    app.run()