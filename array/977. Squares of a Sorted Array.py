class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_square=[]
        for i in nums:
            nums_square.append(i**2)
        return sorted(nums_square)