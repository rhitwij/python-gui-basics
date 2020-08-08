from tkinter import *

root = Tk()

canvas_width = 800

canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("gui12")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()


#The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400 , fill="red")
can_widget.create_line(0, 400, 800, 0, fill="blue")

#to create a rectangle specify parameters in this order - coordinate of top left and coordinate of bottom right.
#can_widget.create_rectangle(3,5,700,300, fill="yellow")

#To create a text coordinate will be centre coordinate.like x1,y1 whre x1 = y1
can_widget.create_text(200,200,text="FUCK YOU")

#coordinate is like rectangle 4 parameters
can_widget.create_oval(344,233,244,355)# if you need a circle u have to give coordinate of square like top left and bottom right

root.mainloop()