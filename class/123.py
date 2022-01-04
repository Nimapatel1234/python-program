class atm():
    def __init__(self,b):
        self.b=b
    def withdraw(self):
        c=int(input("enter a amount:"))
        self.b-=c
        return self.b
    def deposit(self):
        self.b+=300
        return self.b
obj=atm(10000)
for i in range(3):
    a=int(input("enter a pin code:"))
    if a==1234:
        print('correct')
        break
    else:
        print('incorrect')
while True:
    obj=atm(10000)
    d=int(input("enter a 1 for bal 2 for withdraw 3 for deposit 4 for exit"))
    
         