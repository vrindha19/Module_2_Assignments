from tkinter import*
from tkinter import messagebox
root=Tk()
def callback():
    messagebox.showinfo("well done great")
    print("you clinked delete")
Button1=Button(root,text="delete",command=callback)
Button1.grid(row=0,column=0,padx=90,pady=50)
root.geometry('200x350')
root.title("python message tkinter")
root.mainloop()