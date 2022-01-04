import sqlite3

def connection():
    a=sqlite3.connect('student.db')
    return a

def create_t(a):
    a.execute('''CREATE TABLE STUDENT(ENROL INT,NAME TEXT,SUBJECT TEXT,MARKS INT)''')
    print("done")

def insert(a):
    f=int(input("enter no:"))
    i=1
    while i<=f:
        p=int(input("enert enrol:"))
        q=input("enter name")
        r=input("enter subject: ")
        s=int(input("enter marks:"))
    a.execute( "INSERT INTO STUDENTS(ENROL,NAME,SUBJECT,MARKS) VALUES(?,?)",(z,i))
    i=i+1
    print("inserted")


o=connection()
insert(o)
o.commit()
o.close()
def delete(a):
    a.execute('DELETE  FROM STUDENT WHERE ENROL=21')
    a.commit
    print("total no of rows deleted:",a.total_changes)
    i=a.execute('SELECT * FROM STUDENT ')
    for record in i:
        print(record)
