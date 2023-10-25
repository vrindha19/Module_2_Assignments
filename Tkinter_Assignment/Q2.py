
from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Include Help")
def get_value():
    name=Text_Area.get()
    
    root2=Tk()
    root2.geometry("500x500")
    root2.title("Include Help")
    label2=Label(root2,text=f"Welcome To Include Help {name}")
    label2.place(x=160, y=80)
    root2.mainloop()
Text_Area=StringVar()
label=Label(root,text="Enter Your Name")
label.place(x=190,y=80)
Input=Entry(root,textvariable=Text_Area,width=30)
Input.place(x=130,y=100)
button=Button(root,text="Submit",command=get_value,bg="red")
button.place(x=180,y=130)
root.mainloop()