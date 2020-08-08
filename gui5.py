from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("455x244")
#photo = PhotoImage(file="DSCN0884")
#for jpg images
image = Image.open("1.png.JPG")
photo = ImageTk.PhotoImage(image)
L = Label(image=photo)
L.pack()
root.mainloop()