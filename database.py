import sqlite3

CREATE_HW_TABLE = """CREATE TABLE homework IF NOT EXISTS
                    (id INTEGER PRIMARY KEY, course TEXT, type TEXT, time INTEGER);"""

INSERT_HW = "INSERT INTO homework (course, type, time) VALUES (?, ?, ?);"

SHORTEST_HW = "SELECT * FROM homework ORDER BY time DESC LIMIT 1;"

def connect():
    return sqlite3.connect("data.db")

def create_table(connection):
    with connection:
        connection.execute(CREATE_HW_TABLE)

def add_hw(course, type, time):
    with connection:
        connection.execute(INSERT_HW, (course, type, time))

def get_hw(connection):
    with connection:
        return connection.execute(SHORTEST_HW).fetchall()