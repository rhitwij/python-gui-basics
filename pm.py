from tkinter import *
import tkinter

def body():
    sum = int(e1.get()) + int(e2.get())
    ans.set(sum)

root = Tk()
ans = StringVar();
Label(root, text="enter number").grid(row=0, sticky=W)
Label(root, text="enter number").grid(row=1, sticky=W)
Label(root, text="result").grid(row=2, sticky=W)
result = Label(root, text="", textvariable=ans).grid(row=3,column=1,sticky=W)

e1 = Entry(root).grid(row=0,column=1)
e2 = Entry(root).grid(row=1,column=1)

b = Button(root, text="calculate", command=body).grid(row=0,column=2,columnspan=2,rowspan=2,sticky=W+E+N+S,padx=5,pady=5)




mainloop()