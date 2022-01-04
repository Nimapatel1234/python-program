import sqlite3

def connection():
    a=sqlite3.connect('product.db')
    return a

def create_t(a):
    a.execute('''CREATE TABLE PRODUCT(NO INT,NAME TEXT,PRIZE INT)''')
    print("done")

def insert(a):
    f=int(input("enter no of products:"))
    i=1
    while i<=f:
        q=input("enter name of products: ")
        r=int(input("enter prize of products:"))
        a.execute( "INSERT INTO PRODUCT(NAME,PRIZE) VALUES(?,?)",(q,r))
        i=i+1
    print("inserted")
o=connection()
insert(o)
o.commit()
o.close()