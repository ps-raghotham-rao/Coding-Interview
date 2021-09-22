def f(s):
    i=0
    c=0
    n=len(s)
    while(c<n):
        if s[i] == '#' and i-1 == -1:
            s.pop(i)
        elif s[i] == '#':
            s.pop(i)
            s.pop(i-1)
            i-=1
        else:
            i+=1
        c+=1
    return s

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        
        s=f(s)
        t=f(t)
        print(s)
        print(t)
        if s == t:
            return True
        else:
            return False


            