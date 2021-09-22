
    

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a=-99999999999
        for i in range(len(nums)):
            if i == 0:
                ans=nums[i]
                a=max(ans,a)
                continue
            else:
                ans=max(nums[i],ans+nums[i])
                a=max(ans,a)    
            print(ans)
        return a
                
                
            
        