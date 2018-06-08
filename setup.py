#!/usr/bin/env python3
"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app


from setuptools import setup

APP = ['menu.py']
OPTIONS = {}

setup(
    name = "MacFaceID",
    version = "0.0",
    author = "Vasudha Kalia",
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'numpy', 'opencv', 'matplotlib', 'keyring', 'tcl-tk'],
    'includes':['tcl-tl']
}
"""
from setuptools import setup 
APP = ['menu.py'] 
DATA_FILES = [] 
OPTIONS = {'packages': ['tkinter','matplotlib', 'rumps', 'numpy', 'opencv', 'keyring'],'argv_emulation': True} 
setup( 
     app=APP, 
     data_files=DATA_FILES, 
     options={'py2app': OPTIONS},     
     setup_requires=['py2app'], )