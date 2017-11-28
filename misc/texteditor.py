"""A simple text editor made in Python 2.7."""

from os import path, chdir
workingdir = path.join(path.dirname(__file__), 'texts')
chdir(workingdir)

from Tkinter import Tk, Text, Button
import tkFileDialog
root = Tk("Text Editor")

text = Text(root)
text.grid()

def saveas():
    """Save file."""
    try: 
        t = text.get("1.0", "end-1c")  # "1.0" means read from beginning
        # "end-1c" means delete last character
        savelocation = tkFileDialog.asksaveasfilename()
        file1 = open(savelocation, "w")
        file1.write(t)
        file1.close
    except IOError:
        pass

def openfile():
    """Open file."""
    try:
        location = tkFileDialog.askopenfilename()
        file1 = open(location, "r")
        fileContents = file1.read()
        text.delete(1.0, "end")
        text.insert(1.0, fileContents)
    except IOError:
        pass

button = Button(root, text="Open", command=openfile)
button.grid()
button = Button(root, text="Save As", command=saveas)
button.grid()
root.mainloop()

workingdir = path.join(path.dirname(__file__))
chdir(workingdir)
