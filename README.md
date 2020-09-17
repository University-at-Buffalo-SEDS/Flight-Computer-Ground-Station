UB SEDS Flight Computer Ground Station
===

Setup
---

  * Install `pipenv` using your package manager or with `pip install pipenv`.
  * Run `pipenv sync` to set up the virtualenv.
  * Connect the radio serial adapter.
  * Run `./manage.sh run` to start the server.
  * Open the address that it prints in your web browser.

You might have to set the serial port that the server listens on by creating
`config.py` and setting `SERIAL_PORT = "/dev/ttyUSB0"` or similar.

### Windows

Instead of running `pip` directly you can call it as a module through the
Windows `py` wrapper as `py -m pip`.

Instead of using `manage.sh` to start the app, you can run the following
commands in powershell:
```
$Env:FLASK_APP = "."
$Env:FLASK_ENV = "development"
py -m pipenv run flask run
```

The `SERIAL_PORT` config option should be set to the Windows `COM` device name,
e.g. `SERIAL_PORT = "COM0"`.
