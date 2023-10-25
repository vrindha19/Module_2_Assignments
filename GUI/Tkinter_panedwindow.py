from tkinter import*
from tkinter import ttk
root=Tk()
pw=ttk.PanedWindow(root,orient=HORIZONTAL)
pw.pack(fill=BOTH,expand=True)
Frame1=ttk.Frame(pw,relief=SUNKEN)
Frame2=ttk.Frame(pw,relief=SUNKEN)
pw.add(Frame1,weight=1)
pw.add(Frame2,weight=3)
root.geometry("400x240")
root.title("pythonlobby.com")
root.mainloop()