from tkinter import *

root = Tk()

def welcome():
    print("Welcome here")


def greeting():
    print("Greetings from button 2")


def helloprint():
    print("MY NAME IS ABC")


frame = Frame(root, width=300, height= 250)
frame.bind('<Button-1>',welcome)
frame.bind("<Button-2>",greeting)
frame.bind("<Button-3>",helloprint)

root.mainloop()