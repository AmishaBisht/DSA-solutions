
# def moveZeroes(nums):
#     l=0
#     r=0
#     while l<len(nums):
#         if nums[l]==0:
#             nums.pop(l)
#             r+=1
#         else:
#             l+=1
#     nums.extend([0]*r)

#     # return nums
# nums = [0,1,0,3,12]
# print(moveZeroes(nums))

# i = 0
#         count = 0 
#         while i < len(nums):
#             if nums[i] == 0:
#                 nums.pop(i)
#                 count += 1
#             else:
#                 i += 1
#         nums.extend([0]*count) 
class Solution:
    def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0 
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count += 1
            else:
                i += 1
        return nums.extend([0]*count) 
nums = [0,1,0,3,12]
print(Solution.moveZeroes(nums))