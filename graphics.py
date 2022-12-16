# # Tkinter with button action
# import tkinter as tk
# window= tk.Tk();
# label1 =tk.Label(window,text="This is what it is ")
# label1.pack()
# def new_label():
#   Label2 = tk.Label(window,text="Nice Job").pack()
# def new_button():
#   Button2 = tk.Button(window,text="Press it",command=new_label).pack();
# Button = tk.Button(window,text="Click on this button",command = new_button)
# Button.pack()
# window.mainloop()

# Labels with Image in Tkinter
# import tkinter as tk
# window = tk.Tk()
# Images = tk.PhotoImage(file="./cat.gif")
# labelImage = tk.Label(window,image=Images).pack(side="right")
# label1 = tk.Label(window, padx= 10,text="Smelly cat Smelly cat \n What are they feeding you? \n Smelly Cat, Smelly Cat, \n It's not your fault \n They won't take you to the vet You'r obviously not their favourite pet \n Smelly Cat, Smelly Cat, it's not your fault")
# label1.pack();
# window.mainloop()

#Message Widget
# import tkinter as tk
# window = tk.Tk()
# believer = "Whatever it takes\n cause I love the adrenaline in my veins\n I do Whatever it takes \n Cause i love how it feels when I break the chains \n Whatever it takes \n Take me to the top I'm read for \n whatever it takes \n Cause I love the adrenaline in my veins\nI do what it takes"
# msg = tk.Message(window,text=believer)
# msg.config(bg="lightblue",font=('times',20,'italic'))
# msg.pack()
# window.mainloop()

#Radio Button
# import tkinter as tk
# window = tk.Tk()
# v = tk.IntVar()
# v.set(1)

# languages= [("Javascript",1),("Python",2),("Java",3),("C++",4)]

# def showSelection():
#   selection = "You selected "+str(v.get())
#   tk.Label(window,text=selection).pack()

# tk.Label(window,text="Choose your favourite programming language").pack();
# for language,val in languages:
#   tk.Radiobutton(window,text=language,variable=v,value=val,command=showSelection).pack()
# window.mainloop()

# CheckBoxes
# import tkinter as tk
# window = tk.Tk()
# v1 = tk.IntVar()
# v2 = tk.IntVar()
# def var_selection():
#   selection = "You have selected male: %d female: %d"%(v1.get(),v2.get())
#   tk.Label(window,text=selection).pack()

# tk.Checkbutton(window,text="male",variable=v1).pack()
# tk.Checkbutton(window,text="female",variable=v2).pack()
# tk.Button(window,text="Quit",command=quit).pack()
# tk.Button(window,text="show",command=var_selection).pack()
# window.mainloop()

#Entry widget
# import tkinter as tk
# window = tk.Tk()

# def show_entry():
#   tk.Label("First name is %s \n Second Name is: %s "%(e1.get(),e2.get()))

# tk.Label(window,text="firstName").grid(row=0)
# tk.Label(window,text="Last Name").grid(row=1)

# el = tk.Entry(window,command=show_entry).grid(row=0,column=1)
# e2 = tk.Entry(window,command=show_entry).grid(row=1,column=1);
# window.mainloop()

#Text Widget
# BASIC TKINTER
# from tkinter import *
# window = Tk();
# Label1 = Label(window,text="Hello")
# Label1.pack()
# button = Button(window,text="Goodbye",command=exit)
# button.pack()
# window.mainloop()
  
# Button Creation
# from tkinter import *
# window = Tk()
# def new_Label():
#   Label(window,text="Fuck this").pack()
# def new_button():
#   Button(text="nice job",command=new_Label).pack()
# Button(window,text="click Here",command=new_button).pack();
# window.mainloop()

# from tkinter import *
# window = Tk()
# s = Scrollbar(window)
# T = Text(window,height=3,width=50)
# s.pack(side=LEFT,fill=Y)
# T.pack(side=RIGHT,fill=Y)
# s.config(command=T.yview)
# T.config(yscrollcommand=s.set)
# quotes=""" Hamlet: To be, or not to be that is the question: Whether this nobler in themind to suffer or to take arms against a sea of troubles and by opposing end them . To die, to sleep No more and by a slieep to say we end the hearache, and the thousand natual shocks that flesh is heir to. Tis a consummation Devoutly to be wished. """
# T.insert(END,quotes)
# mainloop()

from tkinter import *
win = Tk()
text_v = "Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming."
text_h = """
NASA 
 Google 
Nokia 
Facebook 
 Netflix 
 Expedia 
 Reddit 
 Quora 
 MIT
 Udemy 
 Shutterstock 
Spotify
Amazon
Mozilla
Dropbox"""

# Adding vertical scroll bar
scroll_v = Scrollbar(win)
scroll_v.pack(side=RIGHT,fill=Y)

# Adding Horizontal scroll bar
scroll_h = Scrollbar(win)
scroll_h.pack(side=BOTTOM,fill=X)

text = Text(win,height=400,width=350,yscrollcommand=scroll_v.set,xscrollcommand=scroll_h.set,wrap=NONE)
text.insert(END,text_h);
text.insert(END,text_v);
scroll_h.config(command=text.xview)
scroll_v.config(command=text.yview)
win.mainloop()

#Dialogues and message Box
# from tkinter import *
# from tkinter.messagebox import *
# def callback():
#   showerror("Answer","Sorry no answer available")
# def answer():
#   if(askyesno('verify',"really quit")):
#     showwarning("yeas","Not yet implemented")
#   else:
#     showinfo("no","Quit has been cancelled")
# Button(text="QUIT",command=callback).pack(fill=X)
# Button(text="ANSWER",command=answer).pack(fill=X)
# mainloop()

# from tkinter import *
# from tkinter.filedialog import *

# def callback():
#   name = askopenfilename()
#   print(name)

# Button(text="File open",command=callback).pack()
# mainloop()

# from tkinter import *
# from tkinter.colorchooser import askcolor

# window= Tk()
# def callback():
#   result = askcolor()
#   print(result)
# Button(window,text='choose color',fg="darkgreen", command=callback).pack();
# Button(window,text="Quit",command=exit).pack();
# mainloop()
