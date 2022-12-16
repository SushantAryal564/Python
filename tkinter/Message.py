from tkinter import *
root = Tk()
var = StringVar()
label = Message(root,textvariable=var,relief=RAISED)
var.set("Hey? how you doing")
label.pack()
root.mainloop()