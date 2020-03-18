try:
    # Python 3 (version que tout le monde devrait utiliser !)
    from tkinter import Button
    from tkinter import Entry
    from tkinter import StringVar
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

except ImportError:
    # Python 2
    from Tkinter import Button
    from Tkinter import Entry
    from Tkinter import StringVar
    from Tkinter import Tk
    from tkFileDialog import askopenfilename


FILETYPES = [("text files", "*.txt")]


root = Tk()

filename = StringVar(root)

entry = Entry(root, textvariable=filename)
entry.pack()

# button = Button( root,
#                  text='Open',
#                  lambda: filename.set(askopenfilename(filetypes=FILETYPES)) )
# button.pack()

# Ou alors :


def set_filename():
    filename.set(askopenfilename(filetypes=FILETYPES))


button = Button(root, text='Open', command=set_filename)
button.pack()

root.mainloop()
