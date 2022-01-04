import sqlite3

def connection():
    a=sqlite3.connect('product.db')
    return a

def create_t(a):
    a.execute('''CREATE TABLE PRODUCT(ID INT PRIMARY KEY AUTOINCREMENT,NAME TEXT,SUBJECT TEXT,MARKS INT)''')
    print("done")

def insert(a):
    f=int(input("enter no of product:"))
    i=1
    while i<=f:
        q=input("enter name of product:")
        r=input("enter prize of product: ")
        a.execute( "INSERT INTO PRODUCT(NAME,PRIZE) VALUES(?,?)",(q,r))
        i=i+1
    print("inserted")

o=connection()
insert(o)
o.commit()
o.close()