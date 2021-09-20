def counts(str, ln, p):
    count = 0
 
    for i in range(ln):
        n = 0
 
        for j in range(i, ln):
            n = n * 10 + (ord(str[j]) - ord('0'))
 
            if (n % p == 0):
                count += 1
    
    return count
 

ln,p=map(int,input().split())
str1 = int(input())
str1=str(str1)
print(counts(str1, ln, p))
