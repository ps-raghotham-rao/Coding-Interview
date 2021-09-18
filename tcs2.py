n=int(input())
o = int(input())
o = str(o)
ls=[]
c=0
for i in range(n):
    if o in str(i):
        ls.append(i)
        c+=1
for i in ls:
    print(i,end=' ')
print(c)