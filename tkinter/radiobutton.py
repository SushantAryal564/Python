from tkinter import *
root = Tk()
var = IntVar()
def sel():
  selection="You selected the options"+str(var.get())
  lable.config(text=selection)

R1= Radiobutton(root,text="Java",variable=var,value=1,command=sel)
R1.pack()
R2= Radiobutton(root,text="Python",variable=var,value=2,command=sel)
R2.pack()
R3 = Radiobutton(root,text="Javascript",variable=var,value=3,command=sel)
R3.pack()
lable=Label(root);
lable.pack()
root.mainloop()