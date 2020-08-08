#grid
from tkinter import *
from tkinter import messagebox

def getvals():
    messagebox.showinfo("display", "username = "+uservalue.get())
    messagebox.showinfo("display","password = "+passvalue.get())
#    print("ussername = {uservalue.get()}")
#    print("password = {passvalue.get()}")


root = Tk()
root.geometry("500x400")
user = Label(root, text="username")
password = Label(root, text="password")
user.grid() # .grid() used as .pack()
password.grid(row=1)
# variable class in tkinter
# BooleanVar, IntVar, StringVar, DoubleVar
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text = "submit", command = getvals).grid()


root.mainloop()