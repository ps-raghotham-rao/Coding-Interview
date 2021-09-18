# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         ls=nums[:]
#         # print(ls)
#         for i in range(len(nums)):
#             if i == 0:
#                 continue

#             if ls[i]+ls[i-1] > ls[i]:
#                 ls[i]=ls[i]+ls[i-1]
#         ans=max(ls)
#         return ans
#         # print(ls)
# print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

#if you want array list from where to where. Then max value to just previous same value of nums and ls




class Solution:
    def maxSubArray(self, nums):
        ls=nums[:]
        # print(ls)
        for i in range(len(nums)):
            if i == 0:
                continue

            if ls[i]+ls[i-1] > ls[i]:
                ls[i]=ls[i]+ls[i-1]
        ans=max(range(len(ls)),key=ls.__getitem__)
        print(range(len(ls)))
        ans1=max(ls)
        print(ans,ans1)
        
        # print(ls)
print(Solution().maxSubArray([-2,1,-3,4,-1,2,3,-5,4]))