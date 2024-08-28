from flask import Flask, render_template, request
from utils.translate import translate
from waitress import serve
import webbrowser
from threading import Timer

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html', input='Enter phonetic Tibetan here.', translation='Translation will appear here.')


@app.route('/translate', methods=["POST", "GET"])
def serve_translation():
    input = request.form['input']
    translation = translate(input)
    return render_template('index.html', input=input, translation=translation)


def open_browser():
      webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == '__main__':
    Timer(1, open_browser).start()
    serve(app, host="0.0.0.0", port=5000, url_scheme='https')