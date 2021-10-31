import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = {"packages": ['sys', 'os', 'sqlite3', 'cx_Freeze'],
         "include_files": ['icon.ico', 'gui', 'plumbing.db', 'qt_core.py', 'settings.json', 'fabData.json']}

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "3azmy",
    version = "1.0.0",
    description = "the first shot to make a system",
    author = "M & A",
    options = {'build_exe' : files},
    executables = [target]
    
)