from tkinter import *
import database


def addHw(course, type, time):
    connection = database.connect()
    database.create_table(connection)
    database.add_hw(connection, course, type, time)

def whatToWorkOn():
    output = Text(window)
    output.grid(row=9)
    output.delete(0.0, END)
    connection = database.connect()
    try:
        hw = database.get_hw(connection)
        answer = "you should work on your " + hw[2] +" for "+ hw[1] +"!"
    except:
        answer = "you don't have any homework!"
    output.insert(END, answer)

# main:
window = Tk()
window.title("Homework Tracker")
window.configure(background="pink")
window.geometry('600x600')
window.resizable(0,0)

# title
appTitle = Label(window, text="Here's your own Homework Tracker!",
                 bg="pink", fg="white", font="arial 20 bold")
appTitle.grid(row=0, column=1, columnspan=1, pady=5)

# client options
options = Label(window, text="add homework if you'd like, or find the next piece of homework you should complete!",
                fg="white", bg="pink", font="arial 13 bold")
options.grid(row=1, column=1, columnspan=2, pady=10)

# text entries
course_box = Entry(window, width=30, bg="white", fg="pink")
course_box.grid(row=4)
course = course_box.get()
type_box = Entry(window, width=30, bg="white", fg="pink")
type_box.grid(row=5)
hw_type = type_box.get()
time_box = Entry(window, width=30, bg="white", fg="pink")
time_box.grid(row=6)
time = time_box.get()

# buttons
submit = Button(window, text="Add Homework!", command=addHw(course, hw_type, time), fg="white")
submit.grid(row=7, column=1)
getHW = Button(window, text="What to Work on Next", command=whatToWorkOn())
getHW.grid(row=8, column=1, padx=50, pady=5)


window.mainloop()
