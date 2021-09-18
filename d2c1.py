n=int(input())
ls=list(map(int,input().split()))

d={}
for i in range(0,len(ls)):
    d[ls[i]]=i+1

ls=sorted(d.items())
for i in ls:
    print(i[1],end=' ')
