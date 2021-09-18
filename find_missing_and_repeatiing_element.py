class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        d={}
        for i in range(1,n+1):
            d[i]=0
        
        for i in arr:
            d[i]+=1

        
        for k,v in d.items():
            if v == 2:
                a=k
            if v == 0:
                b=k
        return a,b
        
print(Solution().findTwoElement([2,2],2))