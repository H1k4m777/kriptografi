import tkinter
from tkinter import *
import main

window = tkinter.Tk()
window.title("Kriptografi")
window.geometry("700x300")

def get_entry():
    entryString = E2.get()
    entryInt = int(entryString)
    hsl.config(text= main.encryptRailFence(E1.get(), entryInt))

L1 = Label(window, text = "Plaintext")
L1.grid(row=0,column=0)

L2 = Label(window, text = "Key")
L2.grid(row=1,column=0)

E1 = Entry(window, bd = 5,width=100)
E1.grid(row=0,column=1)

E2 = Entry(window, bd = 5,width=100)
E2.grid(row=1,column=1)

hsl = Label(window, text = "")
hsl.grid(row=3,column=0,columnspan=2)

def get_decode():
    entryString = E2.get()
    entryInt = int(entryString)
    hsl.config(text= main.decryptRailFence(E1.get(), entryInt))

bt1 = Button(window, text= "Enkripsi", command= get_entry)
bt1.grid(row=4,column=0,columnspan=2)

bt2 = Button(window, text= "Dekripsi", command= get_decode)
bt2.grid(row=5,column=0,columnspan=2)

# text = Text(window)
# text.insert(INSERT, main.encryptRailFence(E1.get(), 2))
# text.grid(row=3,column=0,columnspan=2)

window.mainloop()