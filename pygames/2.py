a=[]
s=open('new.txt','r')
l=s.readlines()
s=str(l)
for i in s:
    if not i.isnumeric():
    if not i.isalpha()