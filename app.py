from tkinter import *
from database import *
import sqlite3 as sq

# database commands
CREATE_HW_TABLE = """
CREATE TABLE IF NOT EXISTS homework
(id INTEGER PRIMARY KEY, course TEXT, type TEXT, time INTEGER)"""

INSERT_HW = """
INSERT INTO homework (course, type, time)
 VALUES (?, ?, ?)"""

SHORTEST_HW = """
SELECT * FROM homework
ORDER BY time DESC 
LIMIT 1"""

# database connection
con = sq.connect("data.db", timeout=10)
c = con.cursor()

# set GUI
window = Tk()
window.title("Homework Suggester")
window.geometry("800x600+0+0")
header = Label(window, text="Your Homework Suggester", font=("arial", 30, "bold"),
               fg="goldenrod").pack()

# variable
course = StringVar(window)
hwType = StringVar(window)
time = IntVar(window)
Answer = StringVar(window)

# clear variables
def clear():
    course.set("")
    hwType.set("")
    time.set(0)
    Answer.set("")

# add homework into database
def addHw(course, type, time):
    c.execute(CREATE_HW_TABLE)
    c.execute(INSERT_HW, (course, type, time))
    con.commit()
    clear()

# insert homework into
def insertHw():
    hwAnswer = Text(window)
    hwAnswer.delete(0.0, END)
    try:
        hw = c.execute(SHORTEST_HW).fetchall()
        answer = "You should work on your " + hw[2] + " for "+ hw[1] +"!"
    except:
        answer = "Add homework to find out what to work on next!"
    Answer.set(answer)
    hwAnswer.insert(INSERT, Answer)
    clear()

# labels
courseL = Label(window, text="Course", font=("arial", 20), fg="goldenrod").place(x=10, y=100)
hwTypeL = Label(window, text="Homework Type", font=("arial", 20), fg="goldenrod").place(x=10, y=150)
timeL = Label(window, text="Time required (hours)", font=("arial", 20), fg="goldenrod").place(x=10, y=200)

# entry widgets
courseT = Entry(window, textvariable=course)
courseT.place(x=220, y=105)
hwTypeT = Entry(window, textvariable=hwType)
hwTypeT.place(x=220, y=155)
timeT = Entry(window, textvariable=time)
timeT.place(x=220, y=205)

# buttons
addButton = Button(window, text="Add homework",
                   command=addHw(course.get(), hwType.get(), time.get()))
addButton.place(x=10, y=300)
getButton = Button(window, text="Get homework", command=insertHw())
getButton.place(x=10, y=350)
clearButton = Button(window, text="Clear", command=clear())
clearButton.place(x=10, y=400)

window.mainloop()
