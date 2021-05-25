from tkinter import *
import database

def optionChecker(course, type, time):
    course = course.get()
    time = int(float(time.get()))
    type = type.get()

    connection = database.connect()
    database.create_table(connection)
    database.add_hw(course, type, time)

def hwButtons():
    hw_course = Entry(window, width=30, bg="white", fg="pink")
    hw_course.grid(row=4)
    hw_type = Entry(window, width=30, bg="white", fg="pink")
    hw_type.grid(row=5)
    hw_time = Entry(window, width=30, bg="white", fg="pink")
    hw_time.grid(row=6)

    submit = Button(window, type="submit", command=optionChecker(hw_course, hw_type, hw_time))
    submit.grid(row=7, column=1)


def whatToWorkOn():
    connection = database.connect()
    hw = database.get_hw(connection)
    answer = "you should work on your " + hw[2] +" for "+ hw[1] +"!"
    output = Text(window, wrap=WORD, text=answer)


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
options = Label(window, text="add homework if you'd like, or click,
                fg="white", bg="pink", font="arial 13 bold")
options.grid(row=1, column=1, columnspan=2, pady=10)

# buttons
addToDB = Button(window, text="Add to Homework", command=hwButtons())
addToDB.grid(row=2, column=1, padx=50, pady=5)
getHW = Button(window, text="What to Work on Next", command=whatToWorkOn())
getHW.grid(row=3, column=1, padx=50, pady=5)

window.mainloop()
