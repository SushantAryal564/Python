from tkinter import *
from tkinter import messagebox
root = Tk()
def showinfo():
  messagebox.showinfo("Tkinter","You are using tkinter library for python")
button = Button(root,text="Hello there",command=showinfo)
button.pack()
root.mainloop()
