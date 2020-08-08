from tkinter import * #imported tkinter gui
win = Tk()
#B1 = Button(win, text = 'one')
#B2 = Button(win, text = 'two')
#B1.pack(side=LEFT, padx=10)
#B2.pack(side=LEFT, padx=10)
#B1.grid(row=0, column=0)
#B2.grid(row=1, column=1)
#L = Label(win, text='This is label')
#L.grid(row=1, column=0)
f = Frame(win)
b1 = Button(f, "one")
b2 = Button(f, "two")
b3 = Button(f, "three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
L = Label(win, 'This label is over all button')
L.pack()
f.pack()





