from tkinter import *
root = Tk()
root.geometry("644x434") #(widthxheight)
root.minsize(300, 100)#(width , height)
root.maxsize(1200, 900)#(width, height)
L = Label(text="This is rhitwij")
L.pack()#if we not pack this then gui will not display This is rhitwij.
root.mainloop()