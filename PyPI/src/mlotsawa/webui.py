# Import necessary libraries
from transformers import pipeline
from flask import Flask, render_template, request
from waitress import serve
import webbrowser
from threading import Timer
from datetime import datetime
from pathlib import Path

# Import custom transliteration and translation modules
from mlotsawa.transliterator import Transliterator
from mlotsawa.translator import Translator

# Define a WebUI class to handle the web server and translation functionality
class WebUI():

    def __init__(self):
        # Initialize a Flask application with a static folder for assets
        self.app = Flask(__name__, static_folder='static')

    def run(self, logging=False, log_filepath='mlotsawa_logs.txt', port=5000, autolaunch=True):
        """
        Run the Flask application with optional logging and automatic browser launch.
        Args:
        - logging (bool): If True, enables logging of translation events.
        - log_filepath (str): Path to save log files if logging is enabled.
        - port (int): Port for the Flask application.
        - autolaunch (bool): If True, autolaunch the webui
        """

        # Define the route for the main page, rendering the input form
        @self.app.route('/')
        def index():
            return render_template('index.html', text='Enter Tibetan here.')

        # Define the route to handle translation requests
        @self.app.route('/translate', methods=["POST", "GET"])
        def serve_translation():
            input = request.form['text']  # Get user input from the form
            translation = self.translate(input)  # Perform translation
            if logging:
                self.update_logs(log_filepath)  # Log translation if logging is enabled
            return render_template('index.html', text=translation)  # Render page with translation

        # Function to open a browser tab automatically upon server start
        def open_browser():
            webbrowser.open_new(f"http://127.0.0.1:{port}")

        if autolaunch:
            Timer(1, open_browser).start()  # Start a timer to delay the browser opening

        serve(self.app, host="0.0.0.0", port=port, url_scheme='https')  # Serve the Flask app

    def translate(self, input):
        """
        Translate the provided Tibetan input text to a different format using transliteration and translation.
        Args:
        - input (str): Tibetan text to be translated.
        Returns:
        - output (str): Translated text with transliterations and translations.
        """
        # Clean input text for processing
        input = input.strip()
        input_lst = input.split('\n')

        # Remove unnecessary carriage returns from input list
        for elt in input_lst:
            if elt == '\r':
                input_lst.remove(elt)
            elt.replace('\r', '')

        # Initialize transliterator and translator models
        translator = Translator()
        transliterator = Transliterator()

        # Perform transliteration and translation on the input text
        phonetic_lst = transliterator.transliterate(input_lst)
        translation_lst = translator.translate(input_lst)

        # Combine original, transliterated, and translated texts for output
        output_lst = []
        for i in range(len(input_lst)):
            combo = [input_lst[i], phonetic_lst[i], translation_lst[i]]
            combo = '\n'.join(combo)
            output_lst.append(combo + '\n')

        # Join all pieces of text for final output
        output = '\n'.join(output_lst)
        return output

    def update_logs(self, filepath):
        """
        Update the log file with the timestamp of each translation event.
        Args:
        - filepath (str): Path to the log file.
        """
        now = datetime.now()  # Get the current timestamp
        with open(Path(filepath), 'a') as f:  # Open log file in append mode
            f.write(f'Translation at {now}\n')  # Write timestamped log entry
