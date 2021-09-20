# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i=0
#         c=0
#         while(c<len(nums)):
#             if nums[i] == 0:
#                 x=nums.pop(i)
#                 nums.append(x)
#             else:
#                 i+=1
#             c+=1
#         return nums

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i=0
#         c=0
#         while(c<len(nums)):
#             if nums[i] == 0:
#                 x=nums.pop(i)
#                 nums.append(x)
#             else:
#                 i+=1
#             c+=1
#         return nums


# class Solution:
#     def moveZeroes(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i=0
#         c=0
#         while(i<len(nums)):
#             if nums[i] == 0:
#                 nums.pop(i)
#                 c+=1
#             else:
#                 i+=1
#         # print(nums,c)
#         # print([0]*c)
#         nums[len(nums):]=[0]*c
#         return nums

# print(Solution().moveZeroes([0,1,0,3,12]))


# a=[1,2,3,4,5]
# print(id(a))
# b=[2,1,3]
# a[len(a):]=b
# print(id(a))

# ls=ls+[2,3]
 
# inside ls is different id from outside. As when you assign. The returned list address is different