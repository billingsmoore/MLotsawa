import PySimpleGUI as sg
import os.path
import lotsawa_funcs

# define file list column
file_list_column = [
    [
        sg.Text("Folder"),
        sg.In(
            size=(20,1), 
            enable_events=True, 
            key="-FOLDER-"
            ),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[],
            enable_events=True,
            size=(40,40),
            key='-FILE LIST-'
        )
    ],
]

# define file viewer column
file_viewer_column = [
    [sg.Text("Contens of chosen file:")],
    [sg.Text(size=(70, 1), key="-TOUT-")],
    [sg.Text(size=(70,40),key="-TEXT-")],
    [sg.Button("Translate")]
]

# define translation viewer column
translation_viewer_column = [
    [sg.Text("Translation of chosen file:")],
    [sg.Text(size=(70, 1), key="-TRANSLATION OUT-")],
    [sg.Text(size=(70,40),key="-TRANSLATION TEXT-")]
]

# define window layout
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(file_viewer_column, scrollable=False, vertical_scroll_only=True),
        sg.VSeparator(),
        sg.Column(translation_viewer_column, scrollable=False, vertical_scroll_only=True)
    ]
]


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
            translation = lotsawa_funcs.translate(filename) # TODO
            window["-TRANSLATION TEXT-"].update(translation)
        except:
            pass

window.close()
