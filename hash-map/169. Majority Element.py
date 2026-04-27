class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        n1=len(nums)//2
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for key in freq.keys():
            if freq[key] > n1:
                return key

