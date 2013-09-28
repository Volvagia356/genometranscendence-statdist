Stat Distributor for Genome Transcendence
=========================================

This is a stat distributor for [*Genome Transcendence*](http://dicentis-veritas.blogspot.com/2013/09/genome-transcendence-introduction.html),
a pen-and-paper RPG written by someone I know.

Requirements
------------
* Python 2.7
* Tkinter

Usage
-----
Run `gui.py`, a window should appear, listing all stats in a column.
Each stat is accompanied by 4 buttons. Clicking these buttons will increase/decrease the stat by 1 or 10 points.

The remaining points and total points are displayed at the top of the window.
There is a **Change** button which is used to change the total points.
When clicked, it will display a prompt, asking for a positive integer.
All distributed points will be reset if the total points is changed.

py2exe
------
The provided `setup.py` file is used with py2exe to generate a Windows executable.
Two DDL files, `tcl85.dll` and `tk85.dll` have to be manually located and copied  into the same folder as gui.exe for it to work.