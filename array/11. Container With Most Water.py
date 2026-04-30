class Solution:
    def maxArea(self, height: List[int]) -> int:
        left =0
        right=len(height)-1
        max_area=float('-inf')
        while left<right:
            area=min(height[left],height[right]) * (right-left)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            max_area=max(max_area,area)
        return max_area
      
        #time complexity: O(n)
        #space complexity: O(1) since we are not using any extra space, we are just using two pointers to calculate the area.