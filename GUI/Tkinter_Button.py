from tkinter import*
root=Tk()
root.title("button Tkinter")
def clicked():
    print("l am logined")
btn=Button(root,text="clicked",command=clicked)
btn.pack()
root.geometry('250x300')
root.mainloop()
     