sum1=int(input())
s=1
n=0
while(n<sum1):
    n=s*(s+1)/2
    s+=1
print(s-1)