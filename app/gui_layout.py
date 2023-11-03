import PySimpleGUI as sg

# define file list column
file_list_column = [
    [sg.Text("Folder"),sg.In(size=(20,1),enable_events=True,key="-FOLDER-"),sg.FolderBrowse(),],
    [sg.Listbox(values=[],enable_events=True,size=(40,25),key='-FILE LIST-')],
    [sg.HSeparator(),],
    [sg.Text('Process Information:',size=(40,1),key='-MONITOR HEADER-')],
    [sg.Text(size=(40,15),key='-MONITOR-')],
    [sg.Button("Translate")]
]

# define file viewer column
file_viewer_column = [
    [sg.Text("Contents of chosen file:")],
    [sg.Text(size=(50, 1), key="-TOUT-")],
    [sg.Multiline(size=(50,50),key="-TEXT-", disabled=True, background_color='#ECECEC')],
]

# define translation viewer column
translation_viewer_column = [
    [sg.Text("Translation of chosen file:")],
    [sg.Text(size=(50, 1), key="-TRANSLATION OUT-")],
    [sg.Multiline(size=(50,50),key="-TRANSLATION TEXT-", background_color='#ECECEC')]
]

# define window layout
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(file_viewer_column),
        sg.VSeparator(),
        sg.Column(translation_viewer_column)
    ]
]