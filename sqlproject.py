from tkinter import *
import tkinter.messagebox
import sqlite3
# class for front end UI (user interface)
class product:
    def __init__(self,root):

        self.root = root
        self.root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("1325*690")
        self.root.config(bg="yellow")

if __name__ =='__main__':
    root=Tk()
    application = product(root)
    root.mainloop()


