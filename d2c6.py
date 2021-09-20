n,s=map(int,input().split())
ls=[]
for i in range(n):
    ls.append(int(input()))

ls=sorted(ls)

mini=999999999
s=s-1
for i in range(0,n-s):
    mini=min(mini,ls[i+s]-ls[i])

    
print(mini)