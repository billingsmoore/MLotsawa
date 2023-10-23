import os
# silence TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import PySimpleGUI as sg
import os.path
import lotsawa_funcs
from gui_layout import layout
import pickle
from time import perf_counter

def main():
    # create the window
    window = sg.Window(title='Lotsawa', layout=layout)
    filename = None

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
            window["-TRANSLATION TEXT-"].update('')
            if filename == None:
                # confirm that a file has been selected
                window["-MONITOR-"].update('Please select a file to translate.')
                window.refresh()
            else:
                try:
                    # load english tokenizer
                    info = []
                    info.append('Running...')
                    window["-MONITOR-"].update('\n'.join(info))
                    window.refresh()
                    tic = perf_counter()
                    with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/tokenizers/eng-tokenizer.pickle', 'rb') as handle:
                        eng_tokenizer = pickle.load(handle)
                    toc = perf_counter()
                    info.append(f'English Tokenizer Loaded in {toc - tic:0.3f} seconds')
                except:
                    info.append('English Tokenizer Failed to Load')
                    window["-MONITOR-"].update('\n'.join(info))
                    window["-TRANSLATION TEXT-"].update('Error: Translation Failed')
                    lotsawa_funcs.write_logs(info, window)
                    continue

                try:
                    # load tibetan tokenizer
                    window["-MONITOR-"].update('\n'.join(info) + '\nLoading Tibetan Tokenizer...')
                    window.refresh()
                    tic = perf_counter()
                    with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/tokenizers/tib-tokenizer.pickle', 'rb') as handle:
                        tib_tokenizer = pickle.load(handle)
                    toc = perf_counter()
                    info.append(f'Tibetan Tokenizer Loaded in {toc - tic:0.3f} seconds')
                    window["-MONITOR-"].update('\n'.join(info))
                except:
                    info.append('Tibetan Tokenizer Failed to Load')
                    window["-MONITOR-"].update('\n'.join(info))
                    window["-TRANSLATION TEXT-"].update('Error: Translation Failed')
                    lotsawa_funcs.write_logs(info, window)
                    continue

                try:
                    # load translation model
                    window["-MONITOR-"].update('\n'.join(info) + '\nLoading Translation Model... (This may take a moment.)')
                    window.refresh()
                    tic = perf_counter()
                    tib_eng_translator = tf.keras.models.load_model("/home/j/Documents/Projects/Iron-Bridge/lotsawa/models/tib-eng-translator-0.4.0.keras")
                    toc = perf_counter()
                    info.append(f'Translation Model Loaded in {toc - tic:0.3f} seconds')
                except:
                    info.append('Translation Model Failed to Load')
                    window["-MONITOR-"].update('\n'.join(info))
                    window["-TRANSLATION TEXT-"].update('Error: Translation Failed')
                    lotsawa_funcs.write_logs(info, window)
                    continue

                try:
                    # translate text
                    info.append('Translating Text...')
                    window["-MONITOR-"].update('\n'.join(info))
                    window.refresh()
                    tic = perf_counter()
                    translation = lotsawa_funcs.translate_text(filename, eng_tokenizer, tib_tokenizer, tib_eng_translator, window, info)
                    toc = perf_counter()
                    info.remove('Translating Text...')
                    info.append(f'Text Translated in {toc - tic:0.3f} seconds')
                    window["-MONITOR-"].update('\n'.join(info))
                    window["-TRANSLATION TEXT-"].update(translation)
                    window.refresh()
                except:
                    info.append('Translation Failed')
                    window["-MONITOR-"].update('\n'.join(info))
                    window["-TRANSLATION TEXT-"].update('Error: Translation Failed')
                    lotsawa_funcs.write_logs(info, window)
                    continue

                try:
                    # save translation to output file
                    window["-MONITOR-"].update('\n'.join(info) + '\nSaving Translation...')
                    window.refresh()
                    with open('/home/j/Documents/Projects/Iron-Bridge/lotsawa/outputs/output.txt', 'w') as output:
                        output.writelines(translation)
                    info.append(f'Translation Saved to \'output.txt\'')
                    info.append('Done!')
                    window["-MONITOR-"].update('\n'.join(info))
                    window["-TRANSLATION TEXT-"].update(translation)
                    lotsawa_funcs.write_logs(info, window)
                except:
                    info.append('Failed to Save Translation')
                    window["-MONITOR-"].update('\n'.join(info))
                    window["-TRANSLATION TEXT-"].update('Error: Translation Failed')
                    lotsawa_funcs.write_logs(info, window)
                    continue

        

                
                    

    window.close()

if __name__=='__main__':
    main()