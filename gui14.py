#events
from tkinter import *
def roni(event):
    print(f"you clicked on the button at {event.x},{event.y}")
root = Tk()
root.title("events in tkinter")
root.geometry("644x334")

widget = Button(root, text="Click me me please ")
widget.pack()

widget.bind('<Button-1>', roni)
widget.bind('<Double-1>', quit)
root.mainloop()