from tkinter import *
root = Tk()
root.geometry("444x233")
root.title("My gui with roni") #title changed
#imp Label options
#text - adds_the_text
#bd - background
#fg - foreground
#font - sets the font-> font = ('comicsansms',27, 'bold'), font = 'comicsansms 27 italic'
#padx - x padding
#pady - y padding
#relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text =''' this is roni
\n i am an engineer
\n i like coding''', bg = 'red', fg = 'yellow', padx = '50', pady = '20', font = 'comicsansms 27 italic', borderwidth=3,
                    relief = SUNKEN)
#IMP pack options
# anchor = nw , ne
# side = top, bottom, left, right (by default top)
# fill =
# padx
# pady
title_label.pack(side = 'left', anchor = 'nw', fill = Y, padx = 34, pady = 34)


root.mainloop()