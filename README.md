UB SEDS Flight Computer Ground Station
===

Setup
---

  * Install `pipenv` using your package manager or with `pip install pipenv`.
  * Run `pipenv sync` to set up the virtualenv.
  * Connect the radio serial adapter.
  * Run `pipenv run python -m app` to start the server.
  * Open the address that it prints in your web browser.

You might have to set the serial port that the server listens on by creating
`app/config.py` and setting `SERIAL_PORT = "/dev/ttyUSB0"` or similar.

### Windows

Instead of running `pip` directly you can call it as a module through the
Windows `py` wrapper as `py -m pip`.

You can run the following commands in powershell to start the app:
```
$Env:FLASK_ENV = "development"
py -m pipenv run python -m app
```

The `SERIAL_PORT` config option should be set to the Windows `COM` device name,
e.g. `SERIAL_PORT = "COM0"`.


## Todo

[ ] Graphs for every value
[ ] Add gyroscope XYZ
[ ] Add Acceleration XYZ
[ ] Time Since last packet
[ ] Optional: Weather
[ ] Optional: Dark Mode
[ ] Optional: Update libraries
[ ] Very Optional: 3D rocket model that rotates with data.

## venv setup
1. Create venv: To create your venv, type "python3 -m venv groundstation-venv" into your terminal
2. Activate venv: 
    MacOS/Unix: Type "source groundstation-venv/bin/activate" into your terminal 
    Windows: Type "groundstation-venv\Scripts\activate" into your terminal
3. Download required packages: Type "pip install -r requirements.txt" into your terminal
4. To deactivate venv: Type "deactivate" into your console
