from tkinter import*
root=Tk()
root.title("pythonlobby")
w=Label(root,text="pythonlobby.com",font="60")
w=Pack()
checkbox1=IntVar()
checkbox2=IntVar()
Button0=Checkbutton(root,text="learing",)
Button1=Checkbutton(root,text="Tutorial",
                    variable=checkbox2,
                    onvalue=1,
                    offvalue=0,
                    height=3,
                    width=12)
Button0.pack()
Button1.pack()
root.geometry('320x220')
mainloop()
