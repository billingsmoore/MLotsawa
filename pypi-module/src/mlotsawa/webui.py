from transformers import pipeline
from flask import Flask, render_template, request
from waitress import serve
import webbrowser
from threading import Timer

from  mlotsawa.transliterator import Transliterator
from mlotsawa.translator import Translator

class WebUI():

    def __init__(self):

        self.app = Flask(__name__, static_folder='static')

    def run(self):

        @self.app.route('/')
        def index():
            return render_template('index.html', text='Enter Tibetan here.')


        @self.app.route('/translate', methods=["POST", "GET"])
        def serve_translation():
            input = request.form['text']
            translation = self.translate(input)
            return render_template('index.html', text=translation)


        def open_browser():
            webbrowser.open_new("http://127.0.0.1:5000")

        Timer(1, open_browser).start()
        serve(self.app, host="0.0.0.0", port=5000, url_scheme='https')

    def translate(self, input):

        # clean input for translation
        input = input.strip()
        input_lst = input.split('\n')

        for elt in input_lst:
            if elt=='\r':
                input_lst.remove(elt)
            elt.replace('\r', '')

        # instantiate model classes
        transliterator = Transliterator()
        translator = Translator()

        # transliterate text
        phonetic_lst = transliterator.transliterate(input_lst)

        # create translation
        translation_lst = translator.translate(input_lst)

        # prepare texts for display
        output_lst = []

        for i in range(len(input_lst)):
            combo = [input_lst[i], phonetic_lst[i], translation_lst[i]]
            combo = '\n'.join(combo)
            output_lst.append(combo+'\n')

        output = '\n'.join(output_lst)

        return output