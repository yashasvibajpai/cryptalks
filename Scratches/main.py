from tkinter import *

root = Tk()
topdecor = Label(root, bg="#901C3F")
topdecor.pack(fill=X)

bottomdecor = Label(root, bg="#900C3F")
bottomdecor.pack(side=BOTTOM, fill=X)

leftdecor = Label(root, bg="#FF5733")
leftdecor.pack(side= LEFT, fill=Y)

rightdecor = Label(root, bg="#FF5733")
rightdecor.pack(side=RIGHT, fill=Y)


root.mainloop()
