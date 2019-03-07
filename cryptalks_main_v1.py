# import tkinter module
from tkinter import *
import base64

# creating root object
root = Tk()

# some border decorations
topdecor = Label(root, bg="#900C3F")
topdecor.pack(fill=X)

bottomdecor = Label(root, bg="#900C3F")
bottomdecor.pack(side=BOTTOM, fill=X)

leftdecor = Label(root, bg="#FF5733")
leftdecor.pack(side=LEFT, fill=Y)

rightdecor = Label(root, bg="#FF5733")
rightdecor.pack(side=RIGHT, fill=Y)

# defining size of window
root.geometry("1200x6000")

# setting up the title of window
root.title("Cryptalks v1.0")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

basicframe = Frame(root, width=800, height=700,
                   relief=SUNKEN)
basicframe.pack(side=LEFT)

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
                text="Your Private Talks",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

lblInfo.grid(row=1, column=0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


# exit function
def close():
    root.destroy()


# reset the window
def reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# labels
lblMsg = Label(basicframe, font=('arial', 16, 'bold'),
               text="MESSAGE", bd=16, anchor="w")

lblMsg.grid(row=1, column=0)

txtMsg = Entry(basicframe, font=('arial', 16, 'bold'),
               textvariable=Msg, bd=1, insertwidth=4,
               bg="#D2B4DE", justify='right')

txtMsg.grid(row=1, column=1)

lblkey = Label(basicframe, font=('arial', 16, 'bold'),
               text="KEY", bd=16, anchor="w")

lblkey.grid(row=2, column=0)

txtkey = Entry(basicframe, font=('arial', 16, 'bold'),
               textvariable=key, bd=1, insertwidth=4,
               bg="#D2B4DE", justify='right')

txtkey.grid(row=2, column=1)

lblmode = Label(basicframe, font=('arial', 16, 'bold'),
                text="MODE(e for encrypt, d for decrypt)",
                bd=16, anchor="w")

lblmode.grid(row=3, column=0)

txtmode = Entry(basicframe, font=('arial', 16, 'bold'),
                textvariable=mode, bd=1, insertwidth=4,
                bg="#D2B4DE", justify='right')

txtmode.grid(row=3, column=1)

lblService = Label(basicframe, font=('arial', 16, 'bold'),
                   text="The Result-", bd=16, anchor="w")

lblService.grid(row=2, column=2)

txtService = Entry(basicframe, font=('arial', 16, 'bold'),
                   textvariable=Result, bd=1, insertwidth=4,
                   bg="#D2B4DE", justify='right')

txtService.grid(row=2, column=3)


# Vigenère cipher: Polyalphabetic Substitution


# Function to encode
def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)

        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Function to decode
def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)


def func():
    print("Message= ", (Msg.get()))

    clear = Msg.get()
    k = key.get()
    m = mode.get()

    if m == 'e':
        Result.set(encode(k, clear))
    elif m == 'd':
        Result.set(decode(k, clear))

    # Show message button


btnTotal = Button(basicframe, padx=16, pady=8, bd=3, fg="black",
                  font=('arial', 16, 'bold'), width=16,
                  text="Show Message", bg="#5B2C6F",
                  command=func, relief=GROOVE).grid(row=7, column=0)

btnReset = Button(basicframe, padx=16, pady=8, bd=3,
                  fg="black", font=('arial', 16, 'bold'),
                  width=16, text="Reset", bg="#D35400",
                  command=reset, relief=GROOVE).grid(row=7, column=3)

btnExit = Button(basicframe, padx=16, pady=8, bd=3,
                 fg="black", font=('arial', 16, 'bold'),
                 width=6, text="Exit", bg="#C0392B",
                 command=close, relief=GROOVE).grid(row=7, column=4)

# keeps window opened up
root.mainloop()
