from tkinter import *
root =Tk()

def submit():
    print("Email is:"+emailvalue.get())
    print("Password is:"+passvalue.get())

root.geometry("500x300")

Label(root, text="REGISTER YOUR EMAIL", pady=10, font="comicsansms 20 bold").grid(row=0,column=4)

Label(root, text="EMAIL ID:", font="comicsansms 17 bold").grid(row=1,column=3)
Label(root, text="PASSWORD:", font="comicsansms 17 bold").grid(row=2,column=3)

emailvalue = StringVar()
passvalue = StringVar()

emailentry = Entry(root, textvariable=emailvalue, width=50).grid(row=1,column=4)
passentry = Entry(root, textvariable=passvalue,width=50).grid(row=2,column=4)

Button(root,text="submit", command=submit).grid(row=3,column=4)




root.mainloop()