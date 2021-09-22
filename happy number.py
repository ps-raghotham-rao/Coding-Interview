def f(n):
    s=0
    while(n!=0):
        a=n%10
        s+=a*a
        n=n//10
    return s
class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while(True):
            if n == 1:
                return True
            
            if n in a:
                return False
            
            if n not in a:
                a.add(n)
            
            n=f(n)
            
        