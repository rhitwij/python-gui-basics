#Frame
from tkinter import *
root = Tk()
root.geometry("655x333")
f1 = Frame(root, bg="yellow", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")
f2 = Frame(root, borderwidth=8, bg='blue', relief=SUNKEN)
f2.pack(side=TOP, fill="x")
l1=Label(f1, text="project tkinter = pycharm",font = 'comicsansms 27 italic')
l1.pack(pady=142)
l2=Label(f2, text="welcome to sublime text", font = 'comicsansms 27 italic', fg="red", padx=22)
l2.pack(pady=142)
root.mainloop()