from tkinter import *
root=Tk()
root.geometry("500x400")

def hello():
    print("tum chutiya hoh")

def hi():
    print("bsdk mc bc chaddi chor dhang se kaam karr nhi toh danda niche se uper daal dunga")

f1=Frame(root, borderwidth=6, bg="green", relief=RAISED)
f1.pack(side=TOP, anchor="nw")

b1=Button(f1,fg="red", text="dum hai toh dabale", command=hello)
b1.pack(side=TOP, padx=22)

b2=Button(f1,fg="red", text="gand phat jayega", command=hi)
b2.pack(side=TOP, padx=22)

b3=Button(f1,fg="red", text="print now")
b3.pack(side=TOP, padx=22)

b4=Button(f1,fg="red", text="print now")
b4.pack(side=TOP, padx=22)

root.mainloop()