class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        a_sum=sum(nums)
        e_sum=(n*(n+1))//2
        return e_sum-a_sum
        