from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("NEWS")
image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)
L1 = Label(text="roni times", bg="yellow", fg="black", font = 'comicsansms 70 bold',padx=40)
L1.pack()
L2 = Label(image=photo,)
L2.pack(side="left", anchor="ne")
L3 = Label(text='This is Tiger \n jkkkkdkkkdkdk', font ='comicsansms 50 italic')
L3.pack(side="top", anchor="nw")

root.mainloop()
