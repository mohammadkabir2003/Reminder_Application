from tkinter import *
import time
from tkinter import messagebox

window = Tk()
window.title('Remind me!')
window.geometry("400x600")
title = Label(window, text="Remind me!", bg="white", font="Helvetica 12 bold")
title.pack(pady=15)


def notesapp():
    notes = ntb.get()
    submitlist = ["Tasks to be reminded:", ""]

    if notes == submitlist[0]:
        messagebox.showwarning("!!!", "You have to erase the text and add your text")
    elif notes == submitlist[1]:
        messagebox.showwarning("!!!", "You have not added your tasks")
    else:
        messagebox.showinfo("Next step", "Great!, now you can more on to setting the timer")


n2r = Label(window, text="What to remind?", fg="black", font="Helvetica 8 bold underline")
n2r.pack(pady=5)
ntb = Entry(window, width=50)
ntb.pack(pady=5)
ntb.insert(0, "Tasks to be reminded:")
button0 = Button(window, text="Submit", bg="white", fg="black", font="Helvetica 8", command=notesapp).pack(pady=5)

line1 = Label(window, text="---------------------", font="Helvetica 12 bold").pack(pady=1)

Label(window, text="Set a timer", fg="black", font="Helvetica 8 bold underline").pack(pady=5)

hours = StringVar()
Label(window, text="Hour", fg="black", font="Helvetica 8 bold").place(x=133, y=207)
Entry(window, textvariable=hours, width=2, font='Helvetica 10').place(x=140, y=229)
hours.set('00')
minutes = StringVar()
Label(window, text="Minute", fg="black", font="Helvetica 8 bold").pack(pady=1)
Entry(window, textvariable=minutes, width=2, font='Helvetica 10').pack(pady=1)
minutes.set('00')
seconds = StringVar()
Label(window, text="Second", fg="black", font="Helvetica 8 bold").place(x=236, y=207)
Entry(window, textvariable=seconds, width=2, font='Helvetica 10').place(x=240, y=229)
seconds.set('00')


def timer():
    time1 = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    while time1 > -1:
        minute, second = (time1 // 60, time1 % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        seconds.set(second)
        minutes.set(minute)
        hours.set(hour)
        window.update()
        time.sleep(1)
        if time1 == 0:
            seconds.set('00')
            minutes.set('00')
            hours.set('00')
            messagebox.showinfo("Timer", "Time's up! Check in later with the checklist.")
        time1 -= 1


Button(window, text='Start', bg="white", fg="black", font="Helvetica 8", command=timer).pack(pady=10)

line2 = Label(window, text="---------------------", font="Helvetica 12 bold").pack(pady=1)

checklist = Label(window, text="Let's check in when the timer is up", fg="black", font="Helvetica 12 bold underline")
checklist.pack(pady=5)


def message():
    msgwindow = Tk()
    msgwindow.title('!!!')
    msgwindow.geometry("200x50")
    Label(msgwindow, text=checkvar.get()).pack()


def help():
    respond = anyleft1.get()
    submitlist1 = ["Yes", "No"]
    if respond == submitlist1[0]:
        import Yes
    elif respond == submitlist1[1]:
        import tkinter
        import No
    else:
        import tkinter
        nonelabel = tkinter.Label(window, text="Please enter Yes or No")
        nonelabel.pack()


anyleft = Label(window, text="Do you have any tasks left? (Yes/No)", fg="black", font="Helvetica 8")
anyleft.pack(pady=5)
anyleft1 = Entry(window, width=50)
anyleft1.pack(pady=5)
button3 = Button(window, text="Submit", bg="white", fg="black", font="Helvetica 8", command=help).pack(pady=5)

checkvar = StringVar()
checkbox1 = Checkbutton(window, text="I have completed all my tasks", font="Helvetica 8", variable=checkvar,
                        onvalue="Great Job").pack(pady=5)
checkbox2 = Checkbutton(window, text="I have not completed any of my tasks", font="Helvetica 8", variable=checkvar,
                        onvalue="Well, you should get started").pack(pady=5)
button2 = Button(window, text="Submit", bg="white", fg="black", font="Helvetica 8", command=message).pack(pady=5)

window.mainloop()
