from tkinter import *
root = Tk()
root.minsize(400,300)
root.maxsize(400,300)
def good():
    with open("CREDITS", 'a') as f:
        f.write(f"Good \n")


def bad():
    with open("CREDITS", 'a') as f:
        f.write(f"BAD \n")

def moderate():
    with open("CREDITS", 'a') as f:
        f.write(f"MODERATE \n")


Button(root, text="GOOD", font="comicsansms 10 bold", background="green", foreground="white",
           command=good).pack(side=LEFT,anchor="nw",padx=5,pady=20)
Button(root, text="OKAY", font="comicsansms 10 bold", background="red", foreground="white",
           command=bad).pack(side=LEFT,anchor="nw",padx=5,pady=20)
Button(root, text="BAD ", font="comicsansms 10 bold", background="orange", foreground="white",
           command=moderate).pack(side=LEFT,anchor="nw",padx=5,pady=20)


root.mainloop()