# nums=[-7,-3,2,3,11]
# Sqr_nums=[]
# n=len(nums)
# for i in range(n):
#     nums[i]=nums[i]*nums[i]
#     Sqr_nums.append(nums[i])


# Sqr_nums.sort()
# print("the", Sqr_nums)

class Solution:
    def sortedSquares(nums):
        Sqr_nums=[]
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]*nums[i]
            Sqr_nums.append(nums[i])
        Sqr_nums.sort()
        Sqr_nums()
nums=[-7,-3,2,3,11]            
print(Solution.sortedSquares(nums.sort()))

    
