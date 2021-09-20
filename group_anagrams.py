class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            stri=""
            for j in sorted(i):
                stri+=str(j)
            if stri not in d:
                d[stri]=[i]
            else:
                d[stri].append(i)
        ls=[]
        for i,v in d.items():
            ls.append(v)
        ls=sorted(ls,key=lambda x:len(x))
        return ls     
    
        
        
        