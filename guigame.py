import tkinter
from tkinter import *
import random
from tkinter import messagebox
from PIL import Image,ImageTk
answers=[
    "python",
    "java",
    "github",
    "tkinter",
    "RPA",
    "array",
    "list",
    "sun",
    "moon",
    "light",
    "computer"
]

words=[
    "onthyp",
    "ajav",
    "bhiutg",
    "ertnkit",
    "ARP",
    "yarra",
    "tisl",
    "uns",
    "oomn",
    "thgil",
    "tercompu"
]

num = random.randrange(0,11,1)

def res():
    global words,answers,num
    num=random.randrange(0,11,1)
    lable.config(text=words[num])
    e1.delete(0,END)

def default():
    global words,answers,num
    lable.config(text=words[num])

def checkans():
    global words,answers,num
    var= e1.get()
    if var == answers[num]:
        messagebox.showinfo("success","This is correct answers")
        res()
    else:
        messagebox.showerror("error","Not correct")
        e1.delete(0,END)




root=tkinter.Tk()
root.geometry("350x400+400+300")
root.minsize(350,400)
#root.maxsize(240,290)
#root.minsize(240,290)
root.title("Tiger jumbled")
root.configure(bg="orange")

lable = Label(root,
              text="Your here",
              font=("verdana,18"),
              bg="white",fg="green", width=15)
lable.pack(pady=10)

ans1=StringVar()

e1=Entry(
    root,
    font="verdana,16", relief=SUNKEN, textvariable=ans1)
e1.pack(ipady=5,ipadx=5) #internal padding

check=Button(
    root,
    text="CHECK",
    font="comicsansms,16,italic",
    width=10,
    bg="Red",
    fg="Yellow",
    relief=RAISED,
    command=checkans)
check.pack(pady=15, anchor="nw", side=RIGHT)

reset=Button(
    root,
    text="RESET",
    font="comicsansms,16,italic",
    width=10,
    bg="Red",
    fg="Yellow",
    relief=RAISED,
    command=res)
reset.pack(pady=15, anchor="ne", side=LEFT)

image=Image.open("photo.jpg")
photo=ImageTk.PhotoImage(image)
L = Label(image=photo)
L.pack(side=BOTTOM, fill="y")

default()



root.mainloop()