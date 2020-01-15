import atexit
from datetime import datetime
from threading import Thread, Event
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_pyfile("config.py")

socketio = SocketIO(app)

from . import views, serial

Thread(target=serial.read_thread).start()

if __name__ == "__main__":
    socketio.run(app)