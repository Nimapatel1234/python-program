import sqlite3

def connection():
    a=sqlite3.connect('new 2.db')
    return a

def create_t(a):
    a.execute('''CREATE TABLE STUDENT(NAME TEXT,AGE INT)''')
    print("done")


o=connection()
create_t(o)
o.commit()
o.close()