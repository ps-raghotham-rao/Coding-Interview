def func(ls):
    mini=999999999
    miniindex=-1
    # print(ls)
    for i in range(1,(len(ls))):
        twosum = ls[i-1]+ls[i]
        if mini > twosum:
            mini=twosum
            miniindex=i-1

    x=ls.pop(miniindex)
    y=ls.pop(miniindex)

    ls.insert(miniindex,x+y)
    return ls

n=int(input())
ls=list(map(int,input().split()))

nrange = (len(ls)-4)

for i in range(nrange):
        
    ls=func(ls)

print(max(ls)-min(ls))

