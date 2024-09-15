from datetime import datetime

def update_logs():

    now = datetime.now()

    with open('flask-app/logs/logs.txt', 'a') as f:
        f.write(f'Translation at {now}\n')