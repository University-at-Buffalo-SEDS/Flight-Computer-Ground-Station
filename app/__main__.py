from threading import Thread

from .app import app, socketio
from .import serial

Thread(target=serial.read_thread).start()

socketio.run(app)
