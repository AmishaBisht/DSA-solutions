# height = [1,8,6,2,5,4,8,3,7]
# result=0
# l,r=0,len(height)-1
# # while l<r:
# #     area=(r-1)* min(height[l]),min(height[r])
# #     result=max(result, area)
# #     if height[l]<height[r]:
# #         l+=1
# #     else:
# #         r-=1

# print(l)
# print(r)
# # print(min(height[l]))
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result=0
        left,right=0,len(height)-1
        while left<right:
            max_area=(right-left)* min(height[left], height[right])
            result=max(result,max_area)
            if height [left]<height[right]:
                left += 1
            else:
                right -= 1
        return result
                
        