from tkinter import *
root = Tk()
T = Text(root,height=2, width=300)
T.pack()
quote = """HAMLET: To be, or not to be that is the question: Whether this nobler i 
nthe mind to suffer The slings and arrows of outrageous fortune or to take arms against a sea of
troubles And by opposing end them. To die to sleep No more and by a sliip to say we end the heartache,
and the thousand natural shocks That flesh is heir to. 'Tis a consummation Devoutly to be wished."""
T.insert(END,quote)
mainloop()