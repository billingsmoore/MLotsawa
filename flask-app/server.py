from flask import Flask, render_template, request
from utils.translate import translate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', input='', translation='')

@app.route('/translate', methods=["POST", "GET"])
def serve_translation():
    input = request.form['input']
    translation = translate(input)
    return render_template('index.html', input=input, translation=translation)

app.run(host='0.0.0.0', port=5000)