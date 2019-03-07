from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# button1 = Button(topFrame, text="1", fg="red")
button2 = Button(topFrame, text="2", fg="blue")
button3 = Button(topFrame, text="3", fg="green")
button4 = Button(bottomFrame, text="4", fg="black")

button3.pack(side=LEFT, fill=X)
button4.pack(side=BOTTOM, fill=Y)


def welcome():
    print("Welcome here")


def greeting():
    print("Greetings from button 2")


def helloprint():
    print("MY NAME IS ABC")


frame = Frame(root, width=300, height= 250)
frame.bind("<Button-1>",welcome)
frame.bind("<Button-2>",greeting)
frame.bind("<Button-3>",helloprint)

button1 = Button(root, text="print it", command=helloprint)

button1.pack(side=LEFT, fill=X)

button2.pack(side=LEFT, fill=X)
root.mainloop()
