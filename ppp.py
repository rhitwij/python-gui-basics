from tkinter import *
from tkinter import messagebox

root = Tk()
root.maxsize(700,300)

def customerdata():
    #print(namevalue.get())
    #print(descriptionvalue.get())

    with open("userdata", 'a') as f: #open data file to store data
        f.write(f"{namevalue.get(), addresvalue.get(), agevalue.get(), dobvalue.get(), professionvalue.get(),countryvalue.get(),statevalue.get()}\n")
    #messagebox.showinfo("feedback","PLEASE GIVE US FEEDBACK")# msg box to display msg

    #top1 = Toplevel()
    #top1.title("FEEDBACK")
    #Label(top1, text="FEEDBACK:",font="comicsansms 10 bold").grid(row=1, column=1,sticky=NSEW)
    #fvalue = StringVar()
    #Entry(top1, textvariable=fvalue).grid(row=1,column=2,sticky=NSEW)
    #Button(top1, text="SUBMIT", pady=5).grid(row=2,column=2)

    messagebox.showinfo("RATING","RATE US")
    top = Toplevel()
    top.title("RATE US")
    top.minsize(200,100)
    top.maxsize(200,100)
    #rating buttons
    Button(top, text="GOOD", font="comicsansms 10 bold", background="green", foreground="white",
           command=good).pack(side=LEFT,anchor="nw",padx=10,pady=20)
    Button(top, text="OKAY", font="comicsansms 10 bold", background="red", foreground="white",
           command=ok).pack(side=LEFT,anchor="nw",padx=5,pady=20)
    Button(top, text="BAD ", font="comicsansms 10 bold", background="orange", foreground="white",
           command=bad).pack(side=LEFT,anchor="nw",padx=5,pady=20)


def good():
    with open("CREDITS", 'a') as f:#store data in credits files
        f.write(f"good,{namevalue.get()}\n")
    messagebox.showinfo("THANKS", "THANKS FOR YOUR VALUABLE TIME")# display msg
    quit()


def bad():
    with open("CREDITS", 'a') as f:#store data in credits file
        f.write(f"BAD \n")
    messagebox.showinfo("THANKS", "THANKS FOR YOUR VALUABLE TIME")
    quit()

def ok():
    with open("CREDITS", 'a') as f:#store data in credits file
        f.write(f"OKAY \n")
    messagebox.showinfo("THANKS", "THANKS FOR YOUR VALUABLE TIME")
    quit()


Label(root, text="ENTER YOUR DETAILS", font="comicsansms 20 bold").grid(row=0,column=4)

#Label(root, text="GOOD",font="comicsansms 10 bold", pady=5).grid(row=1,column=3)
#Label(root, text="BAD",font="comicsansms 10 bold", pady=5).grid(row=2,column=3)
#Label(root, text="MODERATE",font="comicsansms 10 bold", pady=5).grid(row=3,column=3)

Label(root, text="NAME",font="comicsansms 15 bold").grid(row=1,column=3)
namevalue  = StringVar()
Entry(root, textvariable=namevalue, width=30).grid(row=1, column=4 )


#addres entry
Label(root, text="ADDRES:",font="comicsansms 15 bold").grid(row=2,column=3)
addresvalue = StringVar()
Entry(root, textvariable=addresvalue, width=30).grid(row=2, column=4)

#age entry
Label(root, text="AGE:",font="comicsansms 15 bold").grid(row=3,column=3)
agevalue = StringVar()
Entry(root, textvariable=agevalue, width=30).grid(row=3, column=4)

#dob
Label(root, text="DOB:",font="comicsansms 15 bold").grid(row=3,column=5)
dobvalue = StringVar()
Entry(root, textvariable=dobvalue, width=30).grid(row=3, column=6)

#proffesion
Label(root, text="PROFFESION:",font="comicsansms 15 bold").grid(row=4,column=3)
professionvalue = StringVar()
Entry(root, textvariable=professionvalue, width=30).grid(row=4, column=4)

#country
Label(root, text="COUNTRY:",font="comicsansms 15 bold").grid(row=5,column=3)
countryvalue = StringVar()
Entry(root, textvariable=countryvalue, width=30).grid(row=5, column=4)

#state
Label(root, text="STATE:",font="comicsansms 15 bold").grid(row=6,column=3)
statevalue = StringVar()
Entry(root, textvariable=statevalue, width=30).grid(row=6, column=4)

#submit button
Button(root,text="SUBMIT",font="comicsansms 12 bold", command=customerdata).grid(row=7,column=4)





#Button(root, text="CLICK",font="comicsansms 10 bold", background="green", foreground="white", command=good).grid(row=1,column=1)
#Button(root, text="CLICK", font="comicsansms 10 bold", background="red", foreground="white", command=bad).grid(row=1,column=2)
#Button(root, text="CLICK", font="comicsansms 10 bold", background="orange", foreground="white", command=moderate).grid(row=1,column=3)


#Label(root, text="NAME",font="comicsansms 15 bold").grid(row=4,column=3)
#namevalue  = StringVar()
#Entry(root, textvariable=namevalue, width=30).grid(row=4, column=4)


#description entry and store
#Label(root, text="DESCRIPTION:",font="comicsansms 15 bold").grid(row=5,column=3)
#descriptionvalue = StringVar()
#Entry(root, textvariable=descriptionvalue, width=30).grid(row=5, column=4)

#Button(root,text="SUBMIT",font="comicsansms 12 bold", command=customerdata).grid(row=6,column=4)




root.mainloop()




