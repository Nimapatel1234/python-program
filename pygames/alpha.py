a=open('cat.txt', 'a')
n=input("enter alpha:\n")
a.write('\n'+n)
a.close()

d=open('new.txt', 'r')
s=d.readlines()
print(s)

a=[]
s=open('cat.txt','a')
b=input("enter alphanumber:\n")
a.close()
l=s.readlines()
s=str(l)
for i in s:
    if not i.isalpha():
        a.append(i)
    elif not i.isalpha():
        a.append(i)
c=''.join(a)
print(c)        