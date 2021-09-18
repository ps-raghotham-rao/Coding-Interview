a=[4,2,1]
a=sorted(a)
n=5
ls=[]
for i in range(1,n+1):
    ls.append(i)
print(a,ls)
i=0
j=0
x=[]
while(len(a)!=0 and len(ls)!=0):
    if a[i] == ls[j]:
        ls.pop(j)
        a.pop(i)
    else:
        x.append(ls.pop(j))

x+=ls
print(x)



a=[1,2,4]

n=5
for i in range(1,n+1):
    if i not in a:
        print(i)



#occurence
a=[1,2,3,4,5,1,4]
b=[]
c=[]
for i in a:
    if i in b:
        c.append(i)
    else:
        b.append(i)
print(c)


