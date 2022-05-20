import os
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
if os.path.exists(os.path.join(app.root_path, "config.py")):
    app.config.from_pyfile("config.py")

socketio = SocketIO(app)
