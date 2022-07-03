import tkinter
from tkinter import *
import main

window = tkinter.Tk()
window.title("Kriptografi")
window.geometry("600x500")

def get_entry():
    entryString = E2.get()
    entryInt = int(entryString)
    hsl.config(text= main.encryptRailFence(E1.get(), entryInt))

L1 = Label(window, font=('helvetica', 50, 'bold'), text = "Plaintext", fg="Black", bd=10, anchor='w')
L1.grid(row=0,column=0)

L2 = Label(window, font=('helvetica', 50, 'bold'), text = "Key" ,fg="Black", bd=10, anchor='w')
L2.grid(row=1,column=0)

E1 = Entry(window, font=('arial', 16, 'bold'), bd=10, insertwidth=3, bg="powder blue", justify='left')
E1.grid(row=0,column=1)

E2 = Entry(window, font=('arial', 16, 'bold'), bd=10, insertwidth=3, bg="powder blue", justify='left')
E2.grid(row=1,column=1)

hsl = Label(window, font=('helvetica', 50, 'bold'), text = "", fg="Black", bd=10, anchor='w')
hsl.grid(row=3,column=0,columnspan=2)

def get_decode():
    entryString = E2.get()
    entryInt = int(entryString)
    hsl.config(text= main.decryptRailFence(E1.get(), entryInt))

bt1 = Button(window, padx=16, pady=8, bd=16, fg="black",
            font=('arial', 16, 'bold'), width=9,
            text="Enkripsi", bg="powder blue",
            command= get_decode)
bt1.grid(row=4,column=0,columnspan=2)

bt2 = Button(window, padx=16, pady=8, bd=16, fg="black",
            font=('arial', 16, 'bold'), width=9,
            text="Dekripsi", bg="powder blue",
            command= get_decode)
bt2.grid(row=5,column=0,columnspan=2)



window.mainloop()