from tkinter import*
from tkinter import ttk
root=Tk()
listbox=Listbox(root,width=45,height=15)
listbox.pack(pady=20)
listbox.insert(1,"c")
listbox.insert(1,"c++")
listbox.insert(2,"java")
listbox.insert(3,"python")
root.geometry('400x240')
root.title('pythonlobby.com')
root.mainloop()