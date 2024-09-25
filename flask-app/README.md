This Flask application is a hyper-minimal webserver for MLotsawa.

You can build a binary for the local OS using:

    pyinstaller -w -F --icon=/static/favicon.ico --add-data "templates:templates" --add-data "static:static" server.py