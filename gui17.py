from tkinter import *
root = Tk()
#root.title("code bar")
#root.geometry("400x400")

root.geometry("733x566")
root.title("pycharm")

def myfunc():
    print("bhk")

mymenu = Menu(root)
mymenu.add_command(label="File",command=myfunc)
mymenu.add_command(label="Exit",command=quit)

root.config(menu=mymenu)

root.mainloop()