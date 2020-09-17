import os
from datetime import datetime
from threading import Thread, Event
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
if os.path.exists("config.py"):
    app.config.from_pyfile("config.py")

socketio = SocketIO(app)

from . import views, serial

Thread(target=serial.read_thread).start()
