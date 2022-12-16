from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

root = Tk()
menu = Menu(root)
fileMenu1 = Menu(menu)
fileMenu2 = Menu(menu)

menu.add_cascade(label="file",menu=fileMenu1)
menu.add_cascade(label='toolbox',menu=fileMenu2)

fileMenu1.add_command(label='new')
fileMenu1.add_separator()
fileMenu1.add_command(label="open")

fileMenu2.add_command(label="Buffer")
fileMenu2.add_separator()
fileMenu2.add_command(label="Euclidean distance")

mainloop()


