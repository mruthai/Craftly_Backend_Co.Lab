# run.py
from dotenv import load_dotenv
load_dotenv()  # This will load the .env file

from src import app, socketio

if __name__ == '__main__':
    socketio.run(app, debug=True)

