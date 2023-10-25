from tkinter import*
from tkinter import ttk
root=Tk()
label=Label(root,text="image Tkinter").pack(side=TOP,pady=10)
path=PhotoImage(file="image3.jpg")
label_image=Label(root,image=path,width=400,height=400)
label_image.pack()
root.geometry("600x400")
root.title("pythonimageTkinter.com")
root.mainloop()


