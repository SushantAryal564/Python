from tkinter import *
from tkinter import filedialog
def callback():
  name=filedialog.askopenfilename()
  print(name)
root = Tk()
Button(root,text="File open",command=callback).pack()
root.mainloop()