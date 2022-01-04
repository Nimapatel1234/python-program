import sqlite3

def connection():
    a=sqlite3.connect('new.db')
    return a

def create_t(a):
    a.execute('''CREATE TABLE STUDENT(NAME TEXT,AGE INT,count INT)''')
    print("done")

def insert(a):
    z=input("enter name: ")
    i=int(input("enter age:"))
    f=int(input("enter count:"))
    a.execute( "INSERT INTO STUDENT(NAME, AGE) VALUES(?,?)",(z,i))
    print("inserted")


o=connection()
insert(o)
o.commit()
o.close()