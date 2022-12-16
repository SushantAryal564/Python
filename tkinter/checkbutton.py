from tkinter import *
from tkinter import messagebox

root = Tk()
checkVar1 = IntVar()
checkVar2 = IntVar()
c1 = Checkbutton(root,text="Music",variable=checkVar1,onvalue=1,offvalue=0,height=5,width=20)
c2= Checkbutton(root,text="Video",variable=checkVar2,onvalue=1,offvalue=0,height=5,width=50)
c1.pack()
c2.pack()
root.mainloop()