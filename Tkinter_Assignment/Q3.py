# try to configure Label widget with various options like background red and font with times new Roman 18 size

from tkinter import *
root = Tk()
var = StringVar()
label = Label( root, anchor = CENTER , bg = "red", textvariable = var, bd = 18, cursor = "dot")
var.set("Tkinter Label is a widget that is used to implement display boxes where you can place text or images")
label.pack()
root.mainloop()



