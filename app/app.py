import os
from flask import Flask
from flask_socketio import SocketIO

# creates app module
app = Flask(__name__)
# checks for os path at config.py
if os.path.exists(os.path.join(app.root_path, "config.py")):
    app.config.from_pyfile("config.py")

# initializes and assigns socketIO to app module
socketio = SocketIO(app)
