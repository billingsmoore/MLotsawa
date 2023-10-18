import os
# silence TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import PySimpleGUI as sg
import os.path
import lotsawa_funcs
from gui_layout import layout
import pickle

def main():
    # create the window
    window = sg.Window(title='Lotsawa', layout=layout)

    # create event loop
    while True:
        event, values = window.read()

        # end program if user closes window
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        # with a folder selected, make a list of file in folder
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f 
                for f in file_list
                if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith('.txt')
            ]

            window["-FILE LIST-"].update(fnames)

        elif event == "-FILE LIST-":
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(values["-FILE LIST-"][0])

                with open(filename, 'r') as f:
                    contents = f.read()

                window["-TEXT-"].update(contents)
            except:
                pass

        elif event == 'Translate':
            try:
                info = []
                # load english tokenizer
                info.append('Running...')
                window["-MONITOR-"].update('\n'.join(info))
                window.refresh()
                with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/tokenizers/eng-tokenizer.pickle', 'rb') as handle:
                    eng_tokenizer = pickle.load(handle)
                info.append('English Tokenizer Loaded')

                # load tibetan tokenizer
                window["-MONITOR-"].update('\n'.join(info) + '\nLoading Tibetan Tokenizer...')
                window.refresh()
                with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/tokenizers/tib-tokenizer.pickle', 'rb') as handle:
                    tib_tokenizer = pickle.load(handle)
                info.append('Tibetan Tokenizer Loaded')
                window["-MONITOR-"].update('\n'.join(info))

                # load translation model
                window["-MONITOR-"].update('\n'.join(info) + '\nLoading Translation Model...')
                window.refresh()
                tib_eng_translator = tf.keras.models.load_model("/home/j/Documents/Projects/Iron-Bridge/lotsawa/models/tib-eng-translator-0.2.0.keras")
                info.append('Translation Model Loaded')

                # translate text
                window["-MONITOR-"].update('\n'.join(info) + '\nTranslating Text...')
                window.refresh()
                translation = lotsawa_funcs.translate_text(filename, eng_tokenizer, tib_tokenizer, tib_eng_translator, window, info)
                info.append('Text Translated')
                window["-MONITOR-"].update('\n'.join(info))

                window["-TRANSLATION TEXT-"].update(translation)
                window.refresh()
            except:
                window["-TRANSLATION TEXT-"].update('Error: Translation Failed')

    window.close()

if __name__=='__main__':
    main()