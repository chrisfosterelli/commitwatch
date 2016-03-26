from setuptools import setup

APP = [ 'trayapp.py' ]
DATA_FILES = [ 'github0.png', 'github.png' ]
OPTIONS = {
    'argv_emulation' : True,
    'packages' : [ 'rumps' ],
    'plist' : { 'LSUIElement' : True }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={ 'py2app' : OPTIONS },
    setup_requires=[ 'py2app' ],
)
