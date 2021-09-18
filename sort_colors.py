# class Solution:
#     def sortColors(self, nums):
#         nums1=sorted(nums)
#         for i in range(len(nums)):
#             nums[i]=nums1[i]
#         return nums

# print(Solution().sortColors([1,1,2,2,0,0]))




# class Solution:
#     def sortColors(self, nums):
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i] > nums[j]:
#                     temp=nums[i]
#                     nums[i]=nums[j]
#                     nums[j]=temp
#         return nums

# print(Solution().sortColors([1,1,2,2,0,0]))




# class Solution:
#     def sortColors(self, nums):
#         zero=0
#         one=0
#         two=0
#         n=len(nums)
#         for i in range(n):
#             if nums[i] == 0:
#                 zero+=1
#             elif nums[i] == 1:
#                 one+=1
#             else:
#                 two+=1
#         for i in range(n):
#             if zero!=0:
#                 nums[i]=0
#                 zero-=1
#             elif one!=0:
#                 nums[i]=1
#                 one-=1
#             elif two!=0:
#                 nums[i]=2
#                 two-=1


#Submission's code
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         a=0
#         b=0
#         c=0
#         for i in nums:
#             if i==0:
#                 a+=1
#             elif i==1:
#                 b+=1
#             else:
#                 c+=1
#         for i in range(a):
#             nums[i]=0
#         for i in range(b):
#             nums[a+i]=1
#         for i in range(c):
#             nums[a+b+i]=2
