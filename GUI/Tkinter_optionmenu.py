import tkinter 
root=tkinter.Tk()
root.title("tkinter option menu")
root.geometry('700x500')
option_list=["option 1","option 2","option 3","option 4"]
value_inside = tkinter.StringVar(root)
value_inside.set("select an option")
question_menu=tkinter.OptionMenu(root,value_inside,*option_list)
question_menu.pack()
def print_answers():
    print("selected option:{}".format(value_inside.get()))
    return None
submit_button=tkinter.Button(root, text='submit',command=print_answers)
submit_button.pack()
root.mainloop()











