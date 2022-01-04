import random 
class account:
    def __init__(self,id,balance = 10000):
        self.id = id
        self.balance = balance
    def getid(self):
        return self.id

    def getbalance(self):
        return self.balance

    def widthdraw(self, amount):
        self.balance -=amount

    def deposit(self, amount):
         self.balance +=amount
def main():
    account=[]
    for i in range(1000,9999):
        account =account(i,10000)  
        accounts.append(account)   
while True:
    id = int(input("\nenter account pin:"))
    while id < 1000 or id > 9999:
        id = int(input("\ninvalid id..re-enter:"))  
    while True:
        print("enter 1 for balance 2 for widthdraw 3 for deposit 4 for exit")   
        c = int(input("enter no:"))
        for acc in accounts:
            if acc.getid() == id:
               accountobj=acc
               break
        if c==1:              