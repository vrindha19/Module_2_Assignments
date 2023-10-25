from tkinter import*
root=Tk()
label=Label(root,text='python frames',font="60")
label.pack()
bottom_frame = Frame(root,bg="green",width=120,height=100)
bottom_frame.pack(side=LEFT, padx=20)
top_frame=Frame(root, bg="red",width=120,height=100)
top_frame.pack(side=LEFT)

root.geometry("300x150")
root.mainloop()
