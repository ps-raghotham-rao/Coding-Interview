n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
sum=0
t=1
for i in a:
    if i == 30:
        sum=sum+i
        continue
    if sum > i:
        sum=sum-i+30
        i=30
        continue
    if i>sum:
        if i-sum == 30:
            sum=0
            continue
        else:
            t=0
            break
if t == 1:
    print("Transaction successful")
else:
    print("Transaction failed")