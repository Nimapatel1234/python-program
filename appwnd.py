a=open('cat.txt', 'w')
p=int(input("enter number of words"))
i=0
for i in range (p):
    n=input("enter name:")
    a.write('\n'+n)
a.close()
