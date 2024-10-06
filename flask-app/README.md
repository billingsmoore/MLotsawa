This Flask application is a minimal webserver for MLotsawa.

The version in this folder is recommended if you intend to run the webserver locally to be used by other users on your network. 
Otherwise, the WebUI class provided in the [mlotsawa PyPI module](https://pypi.org/project/mlotsawa/) is recommended.

You can build a binary for the local OS using:

    pyinstaller -w -F --icon=/static/favicon.ico --add-data "templates:templates" --add-data "static:static" server.py