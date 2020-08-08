from tkinter import *
root = Tk()

def getvals():
    print("submiting form")

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), em_contactvalue.get(),paymentvalue.get(), foodservicevalue.get()}")


    with open("Records.txt", 'a') as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), em_contactvalue.get(),paymentvalue.get(), foodservicevalue.get()}\n")

root.geometry("700x500")

Label(root, text="wlcm to roni traveles", font="comicsansms 12 bold", pady=15).grid(row=0, column=3)

name = Label(root, text="Name:")

phone = Label(root, text="Phone Number:")

gender = Label(root, text="Gender:")

em_contact = Label(root, text="Emergency Contacts:")

payment = Label(root, text="Payment mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
em_contact.grid(row=4, column=2)
payment.grid(row=5, column=2)


namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
em_contactvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
em_contactentry = Entry(root, textvariable=em_contactvalue)
paymententry = Entry(root, textvariable=paymentvalue)



nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
em_contactentry.grid(row=4, column=3)
paymententry.grid(row=5 ,column=3)

foodservice = Checkbutton(text="want to prebook your meals", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

Button(text="submit to roni travles",command=getvals).grid(row=7, column=3)



root.mainloop()