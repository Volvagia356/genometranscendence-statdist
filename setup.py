from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True, 'dll_excludes':['tcl85.dll','tk85.dll']}},
    windows = [{'script': "gui.py"}],
    zipfile = None,
)
