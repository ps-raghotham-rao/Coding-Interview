class Solution:
    def merge(self,arr1,arr2,n,m):
        ls = []
        i=0
        j=0
        while(i<n and j<m):
            if arr1[i] < arr2[j]:
                ls.append(arr1[i])
                i+=1
            else:
                ls.append(arr2[j])
                j+=1
        if i == n:
            while(j<m):
                ls.append(arr2[j])
                j+=1
        elif j == m:
            while(i<n):
                ls.append(arr1[i])
                i+=1
        if n<m:
            small=n
            large=m
            sa=arr1
            sl=arr2
        else:
            small=m
            large=n
            sa=arr2
            sl=arr1
        
        for i in range(len(arr1)):
            arr1[i]=sa[i]
            

        return arr1,arr2

ls2=[1,3,5,7]
ls1=[0,2,6,8,9]
n=len(ls1)
m=len(ls2)
print(Solution().merge(ls1,ls2,n,m))


class Solution:
    def merge(self,arr1,arr2,n,m):
        ls = []
        i=0
        j=0
        while(i<n and j<m):
            if arr1[i] < arr2[j]:
                ls.append(arr1[i])
                i+=1
            else:
                ls.append(arr2[j])
                j+=1
        if i == n:
            while(j<m):
                ls.append(arr2[j])
                j+=1
        elif j == m:
            while(i<n):
                ls.append(arr1[i])
                i+=1



        for i in range(len(arr1)):
            arr1[i]=ls[i]

        for i in range(len(arr2)):
            arr2[i]=ls[len(arr1)+i]        