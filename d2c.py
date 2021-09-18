import math
n=int(input())
ls=[]
for i in range(n):
    ls.append(int(input()))
ls=sorted(ls)
s=0
for i in range(len(ls)):
    s+=math.ceil((ls[i]+ls[i+1])/2)

print(s)