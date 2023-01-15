from tkinter import *

leftwindow = Tk()
leftwindow.title('Help!')
leftwindow.geometry("200x400")
leftlabel = Label(leftwindow, text="Tasks remaining:", font="Helvetica 12 bold").pack(pady=15)
leftentry = Entry(leftwindow, width=50)
leftentry.pack(pady=15)


def left1():
    newlabel = Label(leftwindow, text=leftentry.get())
    newlabel.pack()


entrybutton = Button(leftwindow, text="Submit", bg="white", fg="black", font="Helvetica 8", command=left1).pack(
    pady=5)

leftwindow.mainloop()