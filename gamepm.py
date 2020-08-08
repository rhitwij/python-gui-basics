from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root = Tk()

root.minsize(500,500)
root.maxsize(500,500)

def operation():
    n3.get()
    if n3 == "+":
        print(n1.get() + n2.get())
        messagebox.showinfo("done")
    elif n3 == "-":
        print(n1.get() - n2.get())



#def display():
#    global a,b
    #a = int(input("type a number"))
    #b = int(input("type a number"))
    #print("type operation")
    #opt = input()
 #   operation()

image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)

f1 = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
f1.pack()


l1 = Label(f1, text="PLUS MINUS", bg="blue", fg="yellow" , font="comicsansms 57 bold" )
l1.pack()


f2 = Frame(root, bg="black", borderwidth=6, relief=SUNKEN)
f2.pack(anchor="nw",pady=2)

l2 = Label(f2,image=photo)
l2.pack(anchor="nw",side=LEFT)

l3 = Label(f2, text="ENTER A NUMBER")
l3.pack()

n1 = IntVar()

e1 = Entry(f2, textvariable=n1)
e1.pack(ipady=6,ipadx=40)

l4= Label(f2, text="ENTER A NUMBER")
l4.pack()

n2 = IntVar()

e2= Entry(f2, textvariable=n2)
e2.pack(ipady=6,ipadx=40)

l4 = Label(f2, text="ENTER A + or - operators")
l4.pack()

n3 = StringVar()

e3 = Entry(f2,textvariable=n3)
e3.pack(ipady=6,ipadx=40)

b1=Button(root,fg="yellow",bg="blue", text="SHOW", command=operation)
b1.pack(side=TOP)

#D = Entry(root)
#D.pack()


root.mainloop()