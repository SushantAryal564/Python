from tkinter import *
from tkinter import messagebox
root = Tk()
def answer():
  messagebox.showerror("Answer","Sorry, no answer available")
def callback():
  if messagebox.askyesno("Verify","Really Quit"):
    messagebox.showwarning("Yes","Not yet implemented")
  else:
    messagebox.showinfo("No","Quit has been cancelled")
    
button1 = Button(root,text="QUIT",command=callback).pack()
button2 = Button(root,text="Answer",command=answer).pack()
root.mainloop()