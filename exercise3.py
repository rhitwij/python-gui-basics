from tkinter import *
from tkinter import messagebox

root=Tk()
root.minsize(350,150)
root.maxsize(350,150)

root.title("JAI SREE RAAM")
def ok():
    messagebox.showinfo("GAU MATA","MUTRA PAAN KRO BALAK MOKSH BY DEFAULT MILEGA")

def cancel():
    messagebox.showinfo("BJP","SALA CANCEL KIYA TU AAJ SE ANTI NATIONAL \n JAI SREE RAAM")

l=Label(text="MOKSH PAANE K LIYE OK DABAYE",font="comicsnssms,30,bold")
l.pack()

f1=Frame(root, borderwidth=6, bg="green", relief=RAISED)
f1.pack()

f2=Frame(root, borderwidth=6, bg="green", relief=RAISED)
f2.pack()

b1=Button(f1,fg="red", text="OK", font="verdana,20,italic", command=ok)
b1.pack()

b2=Button(f2,fg="red", text="CANCEL",font="verdana,20,italic", command=cancel)
b2.pack()












root.mainloop()